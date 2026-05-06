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
        self.generic_visit(node)

    def visit_BinOp(self, node):
        operator_map = {
            ast.Add: "+",
            ast.Sub: "-",
            ast.Mult: "*",
            ast.Div: "/",
            ast.FloorDiv: "//",
            ast.Mod: "%",
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
    "Saraso metodai ir atvirkstinis iteravimas": ["append", "range_atvirksciai"],
    "Aritmetika ir formatavimas": ["+", "-", ":.2f"],
    "Ciklai ir salygos": ["if", "for", "while"],
    "Loginiai operatoriai": ["and", "not"],
}


def normalize_output(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def reference_solution(input_data):
    lines = [line.strip() for line in input_data.strip().splitlines() if line.strip()]
    n, s, t, p = map(int, lines[0].split())

    macu_vardai = []
    macu_taskai = []

    kaupiamoji = 0
    rasta = False
    lyderystes_macas = "NERA"
    dabartine = 0
    ilgiausia = 0
    geriausias_taskai = -1
    blogiausias_taskai = 999999
    geriausias_vardas = ""
    blogiausias_vardas = ""

    output = ["Macu_kronika:"]

    for idx in range(1, n + 1):
        parts = lines[idx].split()
        varzybos = parts[0]
        taskai = int(parts[1])
        klaidos = int(parts[2])
        baudos = int(parts[3])
        laimejo = int(parts[4])

        efektyvumas = taskai - klaidos + baudos
        kaupiamoji += taskai

        if efektyvumas >= 80:
            ivertinimas = "Puikus"
        elif efektyvumas >= 50:
            ivertinimas = "Geras"
        elif efektyvumas >= 20:
            ivertinimas = "Vidutinis"
        else:
            ivertinimas = "Silpnas"

        output.append(f"{varzybos} {taskai} {kaupiamoji} {efektyvumas:.2f} {ivertinimas}")

        macu_vardai.append(varzybos)
        macu_taskai.append(taskai)

        if laimejo == 1:
            dabartine += 1
            if dabartine > ilgiausia:
                ilgiausia = dabartine
        else:
            dabartine = 0

        if not rasta and kaupiamoji > s:
            lyderystes_macas = varzybos
            rasta = True

        if taskai > geriausias_taskai:
            geriausias_taskai = taskai
            geriausias_vardas = varzybos

        if taskai < blogiausias_taskai:
            blogiausias_taskai = taskai
            blogiausias_vardas = varzybos

    # Atvirkstine tvarka
    reversed_names = []
    for i in range(len(macu_vardai) - 1, -1, -1):
        reversed_names.append(macu_vardai[i])

    output.append("")
    output.append("Atvirkstine_tvarka:")
    output.append(" ".join(reversed_names))

    # Treniruociu skaiciavimas
    treniruociu = 0
    likusios = t - kaupiamoji
    while likusios > 0:
        likusios -= p
        treniruociu += 1

    output.append("")
    output.append("Sezono_analize:")
    output.append(f"Bendri_taskai: {kaupiamoji}")
    output.append(f"Lyderystes_macas: {lyderystes_macas}")
    output.append(f"Ilgiausia_serija: {ilgiausia}")
    output.append(f"Treniruociu_iki_tikslo: {treniruociu}")
    output.append(f"Geriausias_macas: {geriausias_vardas} {geriausias_taskai}")
    output.append(f"Blogiausias_macas: {blogiausias_vardas} {blogiausias_taskai}")

    # Selection sort (kopijos)
    sort_vardai = macu_vardai[:]
    sort_taskai = macu_taskai[:]

    for i in range(len(sort_taskai)):
        maks_i = i
        for j in range(i + 1, len(sort_taskai)):
            if sort_taskai[j] > sort_taskai[maks_i]:
                maks_i = j
        sort_taskai[i], sort_taskai[maks_i] = sort_taskai[maks_i], sort_taskai[i]
        sort_vardai[i], sort_vardai[maks_i] = sort_vardai[maks_i], sort_vardai[i]

    output.append("")
    output.append("Lyderiu_lentele:")
    for i in range(len(sort_vardai)):
        output.append(f"{i + 1}. {sort_vardai[i]} {sort_taskai[i]}")

    return "\n".join(output)


def build_fixed_cases():
    return [
        TestCase(
            name="Pavyzdys 1 (lyderystes macas randamas)",
            category="Pavyzdiniai testai",
            input_data=(
                "4 200 400 15\n"
                "Zalgiris 85 5 10 1\n"
                "Rytas 70 8 5 0\n"
                "Wolves 90 3 12 1\n"
                "Neptuno 60 10 8 1\n"
            ),
        ),
        TestCase(
            name="Pavyzdys 2 (lyderystes NERA, 0 treniruociu)",
            category="Pavyzdiniai testai",
            input_data=(
                "3 300 250 20\n"
                "Skycop 95 2 15 1\n"
                "Legia 80 10 5 1\n"
                "Barca 75 6 8 0\n"
            ),
        ),
        TestCase(
            name="Pavyzdys 3 (5 macai, daug treniruociu)",
            category="Pavyzdiniai testai",
            input_data=(
                "5 500 600 10\n"
                "Kaunas 50 15 5 0\n"
                "Vilnius 60 10 8 0\n"
                "Klaipeda 70 5 12 1\n"
                "Siauliai 55 20 3 0\n"
                "Panevezys 80 8 10 1\n"
            ),
        ),
        TestCase(
            name="Vienas macas",
            category="Ribiniai testai",
            input_data=(
                "1 50 200 30\n"
                "Lietuva 80 5 10 1\n"
            ),
        ),
        TestCase(
            name="Visi pralaimeti (serija 0)",
            category="Ribiniai testai",
            input_data=(
                "3 100 200 10\n"
                "Alpha 60 5 3 0\n"
                "Beta 55 10 2 0\n"
                "Gamma 70 3 5 0\n"
            ),
        ),
        TestCase(
            name="Tikslas jau pasiektas (0 treniruociu)",
            category="Ribiniai testai",
            input_data=(
                "2 100 150 10\n"
                "ABC 90 2 5 1\n"
                "DEF 80 3 8 1\n"
            ),
        ),
        TestCase(
            name="Ilga pergaliu serija",
            category="Ribiniai testai",
            input_data=(
                "5 1000 2000 100\n"
                "A 70 0 0 1\n"
                "B 80 0 0 1\n"
                "C 75 0 0 1\n"
                "D 85 0 0 1\n"
                "E 60 0 0 0\n"
            ),
        ),
        TestCase(
            name="Lyderystes slenkstis perzengtas pirmu macu",
            category="Ribiniai testai",
            input_data=(
                "2 30 500 10\n"
                "Vienas 50 3 2 1\n"
                "Du 40 5 5 0\n"
            ),
        ),
        TestCase(
            name="Silpnas ivertinimas ir mazas efektyvumas",
            category="Ribiniai testai",
            input_data=(
                "3 500 300 20\n"
                "X 20 5 3 1\n"
                "Y 25 10 5 0\n"
                "Z 15 3 2 1\n"
            ),
        ),
    ]


def build_hidden_cases():
    rng = random.Random(20260423)
    name_pool = [
        "Zalgiris", "Rytas", "Wolves", "Neptuno", "Skycop", "Legia", "Barca",
        "Kaunas", "Vilnius", "Klaipeda", "Siauliai", "Panevezys", "Utena",
        "Alytus", "Telsiai", "Mazeikiai", "Jonava", "Kedainiai", "Visaginas",
        "Druskininkai", "Birstonas", "Plunge", "Raseiniai", "Anyksciai",
    ]

    tests = []
    for case_index in range(12):
        n = rng.randint(2, 6)
        s = rng.randint(50, 400)
        t = rng.randint(150, 800)
        p = rng.randint(5, 30)
        lines = [f"{n} {s} {t} {p}"]

        for match_index in range(n):
            base_name = name_pool[(case_index * 5 + match_index) % len(name_pool)]
            name = f"{base_name}{match_index + 1}"
            taskai = rng.randint(30, 100)
            klaidos = rng.randint(0, 15)
            baudos = rng.randint(0, 15)
            laimejo = rng.randint(0, 1)
            lines.append(f"{name} {taskai} {klaidos} {baudos} {laimejo}")

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
    s = rng.randint(100, 350)
    t = rng.randint(200, 700)
    p = rng.randint(8, 25)
    name_pool = [
        "Zalgiris", "Rytas", "Wolves", "Neptuno", "Lietuva",
        "Skycop", "Legia", "Barca", "Kaunas", "Vilnius",
    ]

    lines = [f"{n} {s} {t} {p}"]
    for idx in range(n):
        name = name_pool[idx % len(name_pool)]
        taskai = rng.randint(40, 95)
        klaidos = rng.randint(0, 12)
        baudos = rng.randint(0, 12)
        laimejo = rng.randint(0, 1)
        lines.append(f"{name} {taskai} {klaidos} {baudos} {laimejo}")

    return TestCase(
        name="Demo testas",
        category="Demo",
        input_data="\n".join(lines) + "\n",
    )


def inspect_source_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        message = f"{error.msg} (eilute {error.lineno}, stulpelis {error.offset})"
        return source, set(), message

    visitor = FeatureVisitor()
    visitor.visit(tree)

    # Regex papildomos patikros
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
    if re.search(r"\.append\s*\(", source):
        visitor.features.add("append")
    # Atvirkstinis range: range(kas nors, -1, -1) arba range(len(...)-1, -1, -1)
    if re.search(r"range\s*\(.*?-1\s*,\s*-1", source, re.DOTALL):
        visitor.features.add("range_atvirksciai")

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
            "got": result.stderr.strip() or "Programa baige darba su klaida.",
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
        exp_line = expected_lines[index] if index < len(expected_lines) else "<eilutes nera>"
        got_line = got_lines[index] if index < len(got_lines) else "<eilutes nera>"
        if exp_line != got_line:
            return index + 1, exp_line, got_line

    return None


def print_failure_details(test_case, result):
    print(f"    Nepraejus testas: {test_case.name}")
    if result["kind"] == "wrong-answer":
        diff = first_difference(result["expected"], result["got"])
        if diff is not None:
            line_no, exp_line, got_line = diff
            print(f"    Pirma bloga vieta: eilute {line_no}")
            print(f"      Laukta: {exp_line}")
            print(f"      Gauta : {got_line}")
    print("    Ivestis:")
    for line in test_case.input_data.strip().splitlines():
        print(f"      {line}")
    print("    Lauktas output:")
    for line in result["expected"].splitlines():
        print(f"      {line}")
    print("    Gautas output:")
    got_text = result["got"] if result["got"] else "(tuscia isvestis)"
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
            print(f"Nezinomas flag: {argument}")
            print_usage()
            sys.exit(1)
        else:
            positional_args.append(argument)

    if len(positional_args) > 1:
        print("Per daug argumentu.")
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
    print("              KREPŠINIO SEZONO KRONIKA — DEMO")
    print("=" * 64)
    print(f"Paleidžiamas failas: {os.path.basename(target_file)}")

    demo_case = build_demo_case()
    result = run_case(demo_case, target_file)

    print("\nSugeneruota ivestis:")
    print("-" * 64)
    for line in demo_case.input_data.strip().splitlines():
        print(line)

    print("\nProgramos output:")
    print("-" * 64)
    got_text = result["got"] if result["got"] else "(tuscia isvestis)"
    for line in got_text.splitlines():
        print(line)

    if result["kind"] == "ok":
        print("\nRezultatas: output sutampa su tiketimu.")
    elif result["kind"] == "wrong-answer":
        print("\nRezultatas: output nesutampa su tiketimu.")
        diff = first_difference(result["expected"], result["got"])
        if diff is not None:
            line_no, exp_line, got_line = diff
            print(f"Pirma bloga vieta: eilute {line_no}")
            print(f"Laukta: {exp_line}")
            print(f"Gauta : {got_line}")
        print("\nTiketinas output:")
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
        print(f"Tiketasi rasti: {target_file}")
        sys.exit(1)

    if demo_mode:
        run_demo(target_file)
        return

    print("=" * 64)
    print("          KREPŠINIO SEZONO KRONIKA — TIKRINTUVAS")
    print("=" * 64)
    print(f"Tikrinamas failas: {os.path.basename(target_file)}")

    _, features, syntax_error = inspect_source_code(target_file)
    if syntax_error is not None:
        print("\nKodo sintakses klaida:")
        print(syntax_error)
        sys.exit(1)

    all_cases = build_all_cases()
    categories = ["Pavyzdiniai testai", "Ribiniai testai", "Slapti testai"]
    grouped_cases = {category: [] for category in categories}
    for case in all_cases:
        grouped_cases[case.category].append(case)

    passed_tests = 0
    total_tests = len(all_cases)

    for category in categories:
        cases = grouped_cases[category]
        category_passed = 0
        first_failure = None

        for case in cases:
            result = run_case(case, target_file)
            if result["ok"]:
                category_passed += 1
                passed_tests += 1
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
            print(f"  Truksta: {' '.join(missing)}")

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
