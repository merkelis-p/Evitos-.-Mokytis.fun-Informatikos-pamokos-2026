import ast
import os
import random
import re
import subprocess
import sys
from dataclasses import dataclass


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TARGET_FILE = os.path.join(SCRIPT_DIR, "nd1.py")


@dataclass
class TestCase:
    name: str
    category: str
    input_data: str


class FeatureVisitor(ast.NodeVisitor):
    def __init__(self):
        self.features = set()

    def visit_For(self, node):
        self.features.add("for")
        self.generic_visit(node)

    def visit_While(self, node):
        self.features.add("while")
        self.generic_visit(node)

    def visit_Break(self, node):
        self.features.add("break")

    def visit_Continue(self, node):
        self.features.add("continue")

    def visit_If(self, node):
        self.features.add("if")
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            self.features.add("and")
        if isinstance(node.op, ast.Or):
            self.features.add("or")
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.Not):
            self.features.add("not")
        if isinstance(node.op, ast.USub):
            self.features.add("-")
        self.generic_visit(node)

    def visit_BinOp(self, node):
        operator_map = {
            ast.Add: "+",
            ast.Sub: "-",
            ast.Mult: "*",
            ast.Div: "/",
            ast.FloorDiv: "//",
            ast.Mod: "%",
            ast.Pow: "**",
        }
        for operator_type, marker in operator_map.items():
            if isinstance(node.op, operator_type):
                self.features.add(marker)
                break
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        if isinstance(node.op, ast.Add):
            self.features.add("+=")
        if isinstance(node.op, ast.Sub):
            self.features.add("-=")
        self.generic_visit(node)

    def visit_Compare(self, node):
        operator_map = {
            ast.Eq: "==",
            ast.NotEq: "!=",
            ast.Lt: "<",
            ast.Gt: ">",
            ast.LtE: "<=",
            ast.GtE: ">=",
        }
        for operator in node.ops:
            for operator_type, marker in operator_map.items():
                if isinstance(operator, operator_type):
                    self.features.add(marker)
        self.generic_visit(node)


FEATURE_GROUPS = {
    "Aritmetika ir formatavimas": ["+", "-", "*", "/", "//", "%", "**", "+=", "-=", ":.2f"],
    "Palyginimai ir logika": ["==", "!=", "<", ">", "<=", ">=", "and", "or", "not"],
    "Valdymo sakiniai": ["if", "elif", "else", "for", "while", "break", "continue"],
}


def normalize_output(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def reference_solution(input_data):
    lines = [line.strip() for line in input_data.strip().splitlines() if line.strip()]
    n, r, p = map(int, lines[0].split())

    teams = []
    for index in range(1, n + 1):
        name, points, wins, bonuses, penalties, rounds, disk = lines[index].split()
        points = int(points)
        wins = int(wins)
        bonuses = int(bonuses)
        penalties = int(penalties)
        rounds = int(rounds)
        disk = int(disk)

        final_score = points + wins ** 2 + bonuses * 2 - penalties
        average = final_score / rounds
        tens = final_score // 10
        remainder = final_score % 10

        if disk == 1:
            medal = "Diskvalifikuota"
        elif final_score >= 100:
            medal = "Auksas"
        elif final_score >= 80:
            medal = "Sidabras"
        elif final_score >= 60:
            medal = "Bronza"
        else:
            medal = "Be_medalio"

        teams.append(
            {
                "name": name,
                "points": points,
                "wins": wins,
                "bonuses": bonuses,
                "penalties": penalties,
                "rounds": rounds,
                "disk": disk,
                "final_score": final_score,
                "average": average,
                "tens": tens,
                "remainder": remainder,
                "medal": medal,
            }
        )

    output = ["Bronzos_lyga:"]
    for team in teams:
        output.append(
            f"{team['name']} {team['final_score']} {team['average']:.2f} "
            f"{team['medal']} {team['tens']} {team['remainder']}"
        )

    finalists = []
    exact_threshold = 0
    tidy_teams = 0

    for team in teams:
        if team["final_score"] == r:
            exact_threshold += 1

        if team["penalties"] <= 10 and team["disk"] == 0:
            tidy_teams += 1

        if team["disk"] == 1:
            continue

        if team["final_score"] >= r:
            finalists.append(team["name"])

    output.append("")
    output.append("Finalo_komisija:")
    output.append(f"Finalistu_skaicius: {len(finalists)}")
    if finalists:
        output.append(f"Finalistai: {' '.join(finalists)}")
    else:
        output.append("Finalistai: NERA")
    output.append(f"Tiksliai_ant_ribos: {exact_threshold}")
    output.append(f"Tvarkingos_komandos: {tidy_teams}")

    first_over_90 = "NERA"
    for team in teams:
        if team["final_score"] > 90:
            first_over_90 = team["name"]
            break

    risk_teams = 0
    bonus_teams = 0
    for team in teams:
        if team["final_score"] < 50 or team["penalties"] > 20:
            risk_teams += 1
        if team["bonuses"] != 0:
            bonus_teams += 1

    output.append("")
    output.append("Komandu_radaras:")
    output.append(f"Pirma_virs_90: {first_over_90}")
    output.append(f"Rizikos_komandos: {risk_teams}")
    output.append(f"Bonusu_komandos: {bonus_teams}")

    active_teams = [team for team in teams if team["disk"] == 0]

    output.append("")
    output.append("Boss_level:")
    if not active_teams:
        output.append("Silpniausia_komanda: NERA")
        output.append("Treniruociu_iki_finalo: 0")
    else:
        weakest_team = active_teams[0]
        for team in active_teams[1:]:
            if team["final_score"] < weakest_team["final_score"]:
                weakest_team = team

        missing_points = r - weakest_team["final_score"]
        trainings = 0
        while missing_points > 0:
            missing_points -= p
            trainings += 1

        output.append(f"Silpniausia_komanda: {weakest_team['name']}")
        output.append(f"Treniruociu_iki_finalo: {trainings}")

    return "\n".join(output)


def build_fixed_cases():
    return [
        TestCase(
            name="Pavyzdys 1",
            category="Pavyzdiniai testai",
            input_data=(
                "3 80 8\n"
                "Aidas 70 4 1 0 3 0\n"
                "Beta 45 2 1 0 3 0\n"
                "Cyra 78 4 4 0 3 0\n"
            ),
        ),
        TestCase(
            name="Pavyzdys 2",
            category="Pavyzdiniai testai",
            input_data=(
                "4 75 5\n"
                "Nova 60 3 0 5 2 0\n"
                "Orka 72 2 4 0 4 1\n"
                "Pulsar 73 1 1 0 3 0\n"
                "Rytas 74 4 0 25 4 0\n"
            ),
        ),
        TestCase(
            name="Pavyzdys 3",
            category="Pavyzdiniai testai",
            input_data=(
                "2 80 10\n"
                "Zen 80 0 0 0 4 1\n"
                "Yra 50 0 0 0 5 1\n"
            ),
        ),
        TestCase(
            name="Riba ir 0 treniruociu",
            category="Ribiniai testai",
            input_data=(
                "3 70 6\n"
                "Aira 61 1 4 0 2 0\n"
                "Bura 40 3 0 0 4 0\n"
                "Ceta 65 4 0 0 5 0\n"
            ),
        ),
        TestCase(
            name="Silpniausios lygybe",
            category="Ribiniai testai",
            input_data=(
                "3 90 10\n"
                "Asta 50 2 0 0 2 0\n"
                "Bora 50 2 0 0 5 0\n"
                "Cora 80 3 1 0 4 0\n"
            ),
        ),
        TestCase(
            name="Viena aktyvi komanda",
            category="Ribiniai testai",
            input_data=(
                "4 85 7\n"
                "Delta 70 3 0 0 5 1\n"
                "Ema 64 4 1 0 4 0\n"
                "Faza 82 1 2 0 3 1\n"
                "Gija 50 0 0 0 5 1\n"
            ),
        ),
        TestCase(
            name="Nera bonusu",
            category="Ribiniai testai",
            input_data=(
                "3 60 4\n"
                "Hera 45 3 0 0 3 0\n"
                "Iva 48 1 0 21 4 0\n"
                "Jota 52 2 0 0 2 0\n"
            ),
        ),
    ]


def build_hidden_cases():
    rng = random.Random(20260403)
    name_pool = [
        "Astra", "Banga", "Cobra", "Drift", "Eter", "Fluksas", "Gamma", "Helix",
        "Ionas", "Jega", "Kodas", "Lazeris", "Mira", "Nova", "Orion", "Pulsas",
        "Quark", "Ritmas", "Sigma", "Titan", "Ulna", "Vega", "Warp", "Xeno",
        "Yota", "Zenit",
    ]

    tests = []
    for case_index in range(12):
        n = rng.randint(2, 6)
        r = rng.randint(55, 100)
        p = rng.randint(3, 12)
        lines = [f"{n} {r} {p}"]

        for team_index in range(n):
            base_name = name_pool[(case_index * 5 + team_index) % len(name_pool)]
            name = f"{base_name}{team_index}"
            points = rng.randint(25, 100)
            wins = rng.randint(0, 6)
            bonuses = rng.randint(0, 6)
            penalties = rng.randint(0, 25)
            rounds = rng.randint(1, 6)
            disk = rng.randint(0, 1)
            lines.append(
                f"{name} {points} {wins} {bonuses} {penalties} {rounds} {disk}"
            )

        tests.append(
            TestCase(
                name=f"Slaptas testas {case_index + 1}",
                category="Slapti testai",
                input_data="\n".join(lines) + "\n",
            )
        )

    return tests


def build_all_cases():
    return build_fixed_cases() + build_hidden_cases()


def build_demo_case():
    rng = random.Random()
    n = rng.randint(2, 5)
    r = rng.randint(60, 95)
    p = rng.randint(4, 12)
    names = [
        "Astra", "Banga", "Citra", "Drift", "Ema", "Fotonas", "Gamma", "Helis",
        "Ira", "Jota", "Kodas", "Luna", "Mira", "Nova", "Orka", "Puma",
    ]

    lines = [f"{n} {r} {p}"]
    for index in range(n):
        name = f"{names[index]}{rng.randint(1, 9)}"
        points = rng.randint(30, 100)
        wins = rng.randint(0, 6)
        bonuses = rng.randint(0, 5)
        penalties = rng.randint(0, 25)
        rounds = rng.randint(1, 6)
        disk = rng.randint(0, 1)
        lines.append(f"{name} {points} {wins} {bonuses} {penalties} {rounds} {disk}")

    return TestCase(
        name="Demo testas",
        category="Demo",
        input_data="\n".join(lines) + "\n",
    )


def inspect_source_code(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        source = file.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        message = f"{error.msg} (eilutė {error.lineno}, stulpelis {error.offset})"
        return source, set(), message

    visitor = FeatureVisitor()
    visitor.visit(tree)

    if re.search(r"\belif\b", source):
        visitor.features.add("elif")
    if re.search(r"\belse\s*:", source):
        visitor.features.add("else")
    if "+=" in source:
        visitor.features.add("+=")
    if "-=" in source:
        visitor.features.add("-=")
    if ":.2f" in source:
        visitor.features.add(":.2f")

    return source, visitor.features, None


def progress_bar(done, total, width=24):
    if total == 0:
        return "[------------------------]"
    filled = round((done / total) * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def run_case(test_case, target_file):
    expected = normalize_output(reference_solution(test_case.input_data))

    try:
        result = subprocess.run(
            [sys.executable, target_file],
            input=test_case.input_data,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "kind": "timeout",
            "expected": expected,
            "got": "Programa nesustojo per 5 sekundes.",
        }

    if result.returncode != 0:
        return {
            "ok": False,
            "kind": "runtime",
            "expected": expected,
            "got": result.stderr.strip() or "Programa baigė darbą su klaida.",
        }

    got = normalize_output(result.stdout)
    return {
        "ok": got == expected,
        "kind": "wrong-answer" if got != expected else "ok",
        "expected": expected,
        "got": got,
    }


def first_difference(expected, got):
    expected_lines = expected.splitlines()
    got_lines = got.splitlines()
    max_len = max(len(expected_lines), len(got_lines))

    for index in range(max_len):
        expected_line = expected_lines[index] if index < len(expected_lines) else "<eilutės nėra>"
        got_line = got_lines[index] if index < len(got_lines) else "<eilutės nėra>"
        if expected_line != got_line:
            return index + 1, expected_line, got_line

    return None


def print_failure_details(test_case, result):
    print(f"    Nepraėjęs testas: {test_case.name}")
    if result["kind"] == "wrong-answer":
        difference = first_difference(result["expected"], result["got"])
        if difference is not None:
            line_no, expected_line, got_line = difference
            print(f"    Pirma bloga vieta: eilutė {line_no}")
            print(f"      Laukta: {expected_line}")
            print(f"      Gauta : {got_line}")
    print("    Ivestis:")
    for line in test_case.input_data.strip().splitlines():
        print(f"      {line}")
    print("    Lauktas output:")
    for line in result["expected"].splitlines():
        print(f"      {line}")
    print("    Gautas output:")
    got_text = result["got"] if result["got"] else "(tuščia išvestis)"
    for line in got_text.splitlines():
        print(f"      {line}")


def print_usage():
    checker_name = os.path.basename(__file__)
    print("Naudojimas:")
    print(f"  python3 {checker_name}")
    print(f"  python3 {checker_name} nd1.py")
    print(f"  python3 {checker_name} -d")
    print(f"  python3 {checker_name} -d nd1.py")


def parse_cli_args(argv):
    demo_mode = False
    target_file = DEFAULT_TARGET_FILE
    positional_args = []

    for argument in argv:
        if argument in {"-d", "--demo"}:
            demo_mode = True
        elif argument in {"-h", "--help"}:
            print_usage()
            sys.exit(0)
        elif argument.startswith("-"):
            print(f"Nežinomas flag: {argument}")
            print_usage()
            sys.exit(1)
        else:
            positional_args.append(argument)

    if len(positional_args) > 1:
        print("Per daug argumentų.")
        print_usage()
        sys.exit(1)

    if positional_args:
        target_argument = positional_args[0]
        if os.path.isabs(target_argument):
            target_file = target_argument
        else:
            target_file = os.path.join(SCRIPT_DIR, target_argument)

    return demo_mode, target_file


def run_demo(target_file):
    print("=" * 64)
    print("                    ROBOTU ARENOS DEMO REZIMAS")
    print("=" * 64)
    print(f"Paleidžiamas failas: {os.path.basename(target_file)}")

    demo_case = build_demo_case()
    result = run_case(demo_case, target_file)

    print("\nSugeneruota įvestis:")
    print("-" * 64)
    for line in demo_case.input_data.strip().splitlines():
        print(line)

    print("\nProgramos output:")
    print("-" * 64)
    got_text = result["got"] if result["got"] else "(tuščia išvestis)"
    for line in got_text.splitlines():
        print(line)

    if result["kind"] == "ok":
        print("\nRezultatas: output sutampa su tikėtinu.")
    elif result["kind"] == "wrong-answer":
        print("\nRezultatas: output nesutampa su tikėtinu.")
        difference = first_difference(result["expected"], result["got"])
        if difference is not None:
            line_no, expected_line, got_line = difference
            print(f"Pirma bloga vieta: eilutė {line_no}")
            print(f"Laukta: {expected_line}")
            print(f"Gauta : {got_line}")
        print("\nTikėtinas output:")
        print("-" * 64)
        for line in result["expected"].splitlines():
            print(line)
    else:
        print(f"\nRezultatas: {result['kind']}")

    print("=" * 64)


def main():
    demo_mode, target_file = parse_cli_args(sys.argv[1:])

    if not os.path.exists(target_file):
        print("\nNerandu tikrinamo failo.")
        print(f"Tikėtasi rasti: {target_file}")
        sys.exit(1)

    if demo_mode:
        run_demo(target_file)
        return

    print("=" * 64)
    print("                 ROBOTU ARENOS TIKRINTUVAS")
    print("=" * 64)

    print(f"Tikrinamas failas: {os.path.basename(target_file)}")

    _, features, syntax_error = inspect_source_code(target_file)
    if syntax_error is not None:
        print("\nKodo sintaksės klaida:")
        print(syntax_error)
        sys.exit(1)

    all_cases = build_all_cases()
    categories = ["Pavyzdiniai testai", "Ribiniai testai", "Slapti testai"]
    grouped_cases = {category: [] for category in categories}
    for case in all_cases:
        grouped_cases[case.category].append(case)

    passed_tests = 0
    total_tests = len(all_cases)
    hidden_total = len(grouped_cases["Slapti testai"])
    hidden_passed = 0

    for category in categories:
        cases = grouped_cases[category]
        category_passed = 0
        first_failure = None

        for case in cases:
            result = run_case(case, target_file)
            if result["ok"]:
                category_passed += 1
                passed_tests += 1
                if category == "Slapti testai":
                    hidden_passed += 1
            else:
                if first_failure is None:
                    first_failure = (case, result)
                if result["kind"] in {"runtime", "timeout"}:
                    print(f"\n{category}: {progress_bar(category_passed, len(cases))} {category_passed}/{len(cases)}")
                    print_failure_details(case, result)
                    sys.exit(1)

        print(f"\n{category}: {progress_bar(category_passed, len(cases))} {category_passed}/{len(cases)}")
        if first_failure is not None:
            print_failure_details(first_failure[0], first_failure[1])

    feature_total = sum(len(markers) for markers in FEATURE_GROUPS.values())
    feature_passed = 0

    print("\nKodo reikalavimai:")
    print("-" * 64)
    for group_name, markers in FEATURE_GROUPS.items():
        found = [marker for marker in markers if marker in features]
        missing = [marker for marker in markers if marker not in features]
        feature_passed += len(found)
        print(f"{group_name}: {progress_bar(len(found), len(markers))} {len(found)}/{len(markers)}")
        if missing:
            print(f"  Trūksta: {' '.join(missing)}")

    total_points = total_tests * 2 + feature_total
    earned_points = passed_tests * 2 + feature_passed
    percent = round((earned_points / total_points) * 100, 1)

    print("\nSantrauka:")
    print("-" * 64)
    print(f"Testai: {passed_tests}/{total_tests}")
    print(f"Kodo reikalavimai: {feature_passed}/{feature_total}")
    print(f"Bendras rezultatas: {earned_points}/{total_points} ({percent}%)")
    print("=" * 64)


if __name__ == "__main__":
    main()
