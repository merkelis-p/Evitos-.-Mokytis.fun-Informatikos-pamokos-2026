import ast
import os
import re
import subprocess
import sys
from dataclasses import dataclass


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


@dataclass
class TestCase:
    name: str
    input_data: str


@dataclass
class Task:
    file_name: str
    title: str
    tests: list
    demo_case: TestCase
    required_features: list
    reference_solution: callable


# ---------------------------------------------------------------------------
# Feature detection
# ---------------------------------------------------------------------------

class FeatureVisitor(ast.NodeVisitor):
    def __init__(self):
        self.features = set()

    def visit_For(self, node):
        self.features.add("for")
        # nested for detection
        for child in ast.walk(node):
            if isinstance(child, ast.For) and child is not node:
                self.features.add("for_in_for")
                break
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

    def visit_BinOp(self, node):
        operator_map = {
            ast.Mod: "%",
            ast.Add: "+",
            ast.Sub: "-",
            ast.Mult: "*",
            ast.Div: "/",
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
            ast.Gt: ">",
            ast.Lt: "<",
            ast.GtE: ">=",
            ast.LtE: "<=",
            ast.Eq: "==",
            ast.NotEq: "!=",
        }
        for operator in node.ops:
            for operator_type, marker in operator_map.items():
                if isinstance(operator, operator_type):
                    self.features.add(marker)
        self.generic_visit(node)


def inspect_source_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        msg = f"{error.msg} (eilutė {error.lineno}, stulpelis {error.offset})"
        return set(), msg

    visitor = FeatureVisitor()
    visitor.visit(tree)

    if "+=" in source:
        visitor.features.add("+=")
    if "-=" in source:
        visitor.features.add("-=")

    return visitor.features, None


# ---------------------------------------------------------------------------
# Reference solutions
# ---------------------------------------------------------------------------

def _int_lines(input_data):
    return [int(line.strip()) for line in input_data.strip().splitlines() if line.strip()]


def reference_u1(input_data):
    values = _int_lines(input_data)
    S = values[0]
    P = values[1]
    menesiai = 0
    while S > 0:
        S -= P
        menesiai += 1
    return str(menesiai)


def reference_u2(input_data):
    values = _int_lines(input_data)
    n = values[0]
    numbers = values[1:n + 1]
    suma = 0
    praleista = 0
    for x in numbers:
        if x <= 0:
            praleista += 1
            continue
        suma += x
    return f"Suma: {suma}\nPraleista: {praleista}"


def reference_u3(input_data):
    values = _int_lines(input_data)
    n = values[0]
    numbers = values[1:n + 1]
    rastas = None
    for x in numbers:
        if x % 7 == 0:
            rastas = x
            break
    return str(rastas) if rastas is not None else "Nerasta"


def reference_u4(input_data):
    values = _int_lines(input_data)
    a = values[0]
    b = values[1]
    rows = []
    for i in range(1, a + 1):
        rows.append(" ".join(str(i * j) for j in range(1, b + 1)))
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Tasks configuration
# ---------------------------------------------------------------------------

TASKS = {
    "u1.py": Task(
        file_name="u1.py",
        title="Mokėjimų planas",
        tests=[
            TestCase("Bazinis atvejis", "100\n30"),
            TestCase("Tiksliai lygu", "60\n20"),
            TestCase("Vienas mokėjimas", "1\n100"),
            TestCase("Didelė skola", "99\n10"),
            TestCase("Vienas litas", "1000\n1"),
        ],
        demo_case=TestCase("Demo", "100\n30"),
        required_features=["while", "-="],
        reference_solution=reference_u1,
    ),
    "u2.py": Task(
        file_name="u2.py",
        title="Teigiamų filtras",
        tests=[
            TestCase("Mišri įvestis", "6\n3\n-2\n5\n0\n4\n-3"),
            TestCase("Visi neigiami", "3\n-1\n-5\n-3"),
            TestCase("Visi teigiami", "4\n10\n20\n30\n40"),
            TestCase("Su nuliais", "5\n0\n0\n7\n0\n3"),
            TestCase("Vienas skaičius teigiamas", "3\n-10\n5\n-3"),
        ],
        demo_case=TestCase("Demo", "6\n3\n-2\n5\n0\n4\n-3"),
        required_features=["for", "continue", "if", "+="],
        reference_solution=reference_u2,
    ),
    "u3.py": Task(
        file_name="u3.py",
        title="Pirmas tinkamas",
        tests=[
            TestCase("Pirmas ne pirmas", "5\n3\n14\n9\n21\n8"),
            TestCase("Nerasta", "3\n4\n9\n11"),
            TestCase("Pirmas iš karto", "4\n7\n1\n2\n3"),
            TestCase("Tik paskutinis tinka", "4\n1\n2\n3\n28"),
            TestCase("Keli tinkami", "5\n14\n3\n21\n9\n7"),
        ],
        demo_case=TestCase("Demo", "5\n3\n14\n9\n21\n8"),
        required_features=["for", "break", "if", "%"],
        reference_solution=reference_u3,
    ),
    "u4.py": Task(
        file_name="u4.py",
        title="Daugybos lentelė",
        tests=[
            TestCase("3x4", "3\n4"),
            TestCase("2x2", "2\n2"),
            TestCase("1x5", "1\n5"),
            TestCase("5x1", "5\n1"),
            TestCase("4x3", "4\n3"),
        ],
        demo_case=TestCase("Demo", "3\n4"),
        required_features=["for", "for_in_for"],
        reference_solution=reference_u4,
    ),
    "u1-teisingas.py": Task(
        file_name="u1-teisingas.py",
        title="Mokėjimų planas (teisingas)",
        tests=[
            TestCase("Bazinis atvejis", "100\n30"),
            TestCase("Tiksliai lygu", "60\n20"),
            TestCase("Vienas mokėjimas", "1\n100"),
            TestCase("Didelė skola", "99\n10"),
            TestCase("Vienas litas", "1000\n1"),
        ],
        demo_case=TestCase("Demo", "100\n30"),
        required_features=["while", "-="],
        reference_solution=reference_u1,
    ),
    "u2-teisingas.py": Task(
        file_name="u2-teisingas.py",
        title="Teigiamų filtras (teisingas)",
        tests=[
            TestCase("Mišri įvestis", "6\n3\n-2\n5\n0\n4\n-3"),
            TestCase("Visi neigiami", "3\n-1\n-5\n-3"),
            TestCase("Visi teigiami", "4\n10\n20\n30\n40"),
            TestCase("Su nuliais", "5\n0\n0\n7\n0\n3"),
            TestCase("Vienas skaičius teigiamas", "3\n-10\n5\n-3"),
        ],
        demo_case=TestCase("Demo", "6\n3\n-2\n5\n0\n4\n-3"),
        required_features=["for", "continue", "if", "+="],
        reference_solution=reference_u2,
    ),
    "u3-teisingas.py": Task(
        file_name="u3-teisingas.py",
        title="Pirmas tinkamas (teisingas)",
        tests=[
            TestCase("Pirmas ne pirmas", "5\n3\n14\n9\n21\n8"),
            TestCase("Nerasta", "3\n4\n9\n11"),
            TestCase("Pirmas iš karto", "4\n7\n1\n2\n3"),
            TestCase("Tik paskutinis tinka", "4\n1\n2\n3\n28"),
            TestCase("Keli tinkami", "5\n14\n3\n21\n9\n7"),
        ],
        demo_case=TestCase("Demo", "5\n3\n14\n9\n21\n8"),
        required_features=["for", "break", "if", "%"],
        reference_solution=reference_u3,
    ),
    "u4-teisingas.py": Task(
        file_name="u4-teisingas.py",
        title="Daugybos lentelė (teisingas)",
        tests=[
            TestCase("3x4", "3\n4"),
            TestCase("2x2", "2\n2"),
            TestCase("1x5", "1\n5"),
            TestCase("5x1", "5\n1"),
            TestCase("4x3", "4\n3"),
        ],
        demo_case=TestCase("Demo", "3\n4"),
        required_features=["for", "for_in_for"],
        reference_solution=reference_u4,
    ),
}


# ---------------------------------------------------------------------------
# Runner helpers
# ---------------------------------------------------------------------------

def normalize_output(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def run_case(task, target_file, test_case):
    expected = normalize_output(task.reference_solution(test_case.input_data))

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
        return {"ok": False, "kind": "timeout", "expected": expected,
                "got": "Programa nesustojo per 5 sekundes."}

    if result.returncode != 0:
        return {"ok": False, "kind": "runtime", "expected": expected,
                "got": result.stderr.strip() or "Programa baigė darbą su klaida."}

    got = normalize_output(result.stdout)
    return {"ok": got == expected, "kind": "ok" if got == expected else "wrong-answer",
            "expected": expected, "got": got}


def first_difference(expected, got):
    exp_lines = expected.splitlines()
    got_lines = got.splitlines()
    for i in range(max(len(exp_lines), len(got_lines))):
        e = exp_lines[i] if i < len(exp_lines) else "<eilutės nėra>"
        g = got_lines[i] if i < len(got_lines) else "<eilutės nėra>"
        if e != g:
            return i + 1, e, g
    return None


def progress_bar(done, total, width=24):
    if total == 0:
        return "[" + "-" * width + "]"
    filled = round((done / total) * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def feature_label(f):
    return "for_in_for" if f == "for_in_for" else f"`{f}`"


# ---------------------------------------------------------------------------
# Demo mode
# ---------------------------------------------------------------------------

def run_demo(task_names):
    print("=" * 64)
    print("          PAMOKOS UZDAVINIU DEMO REZIMAS")
    print("=" * 64)

    for task_name in task_names:
        task = TASKS[task_name]
        target_file = os.path.join(SCRIPT_DIR, task.file_name)

        print(f"\n{task.file_name} — {task.title}")
        print("-" * 64)

        if not os.path.exists(target_file):
            print("Failo nėra.")
            continue

        features, syntax_error = inspect_source_code(target_file)
        if syntax_error is not None:
            print("Kodo sintaksės klaida:")
            print(syntax_error)
            continue

        result = run_case(task, target_file, task.demo_case)

        print("Įvestis:")
        for line in task.demo_case.input_data.strip().splitlines():
            print(f"  {line}")

        print("Programos output:")
        got_text = result["got"] if result["got"] else "(tuščia išvestis)"
        for line in got_text.splitlines():
            print(f"  {line}")

        if result["kind"] == "ok":
            print("Rezultatas: output sutampa su tikėtinu.")
        else:
            print(f"Rezultatas: {result['kind']}")
            if result["kind"] == "wrong-answer":
                diff = first_difference(result["expected"], result["got"])
                if diff is not None:
                    line_no, exp_line, got_line = diff
                    print(f"Pirma bloga vieta: eilutė {line_no}")
                    print(f"Laukta: {exp_line}")
                    print(f"Gauta : {got_line}")
            print("Tikėtinas output:")
            for line in result["expected"].splitlines():
                print(f"  {line}")

        missing = [f for f in task.required_features if f not in features]
        if missing:
            print(f"Trūkstami požymiai: {' '.join(feature_label(f) for f in missing)}")

    print("\n" + "=" * 64)


# ---------------------------------------------------------------------------
# Full check mode
# ---------------------------------------------------------------------------

def run_full_check(task_names):
    print("=" * 64)
    print("           PAMOKOS UZDAVINIU TIKRINTUVAS")
    print("=" * 64)

    total_tests_passed = 0
    total_tests = 0
    total_features_found = 0
    total_features = 0
    files_ok = 0

    for task_name in task_names:
        task = TASKS[task_name]
        target_file = os.path.join(SCRIPT_DIR, task.file_name)

        print(f"\n{task.file_name} — {task.title}")
        print("-" * 64)

        if not os.path.exists(target_file):
            print("Failo nėra.")
            total_tests += len(task.tests)
            total_features += len(task.required_features)
            continue

        features, syntax_error = inspect_source_code(target_file)
        if syntax_error is not None:
            print("Kodo sintaksės klaida:")
            print(syntax_error)
            total_tests += len(task.tests)
            total_features += len(task.required_features)
            continue

        passed = 0
        first_failure = None

        for test_case in task.tests:
            total_tests += 1
            result = run_case(task, target_file, test_case)
            if result["ok"]:
                passed += 1
                total_tests_passed += 1
            elif first_failure is None:
                first_failure = (test_case, result)

        print(f"Testai: {progress_bar(passed, len(task.tests))} {passed}/{len(task.tests)}")

        if first_failure is not None:
            tc, res = first_failure
            print(f"  Nepraėjęs: {tc.name}")
            if res["kind"] == "wrong-answer":
                diff = first_difference(res["expected"], res["got"])
                if diff is not None:
                    line_no, exp_line, got_line = diff
                    print(f"  Pirma bloga vieta: eilutė {line_no}")
                    print(f"    Laukta: {exp_line}")
                    print(f"    Gauta : {got_line}")
            elif res["kind"] in ("runtime", "timeout"):
                print(f"  {res['got']}")
            print("  Tikėtinas output:")
            for line in res["expected"].splitlines():
                print(f"    {line}")

        found = [f for f in task.required_features if f in features]
        missing = [f for f in task.required_features if f not in features]
        total_features += len(task.required_features)
        total_features_found += len(found)

        print(
            f"Požymiai: {progress_bar(len(found), len(task.required_features))} "
            f"{len(found)}/{len(task.required_features)}"
        )
        if missing:
            print(f"Trūksta: {' '.join(feature_label(f) for f in missing)}")

        if passed == len(task.tests) and not missing:
            files_ok += 1

    print("\nSantrauka:")
    print("-" * 64)
    print(f"Failai be klaidų: {files_ok}/{len(task_names)}")
    print(f"Testai: {total_tests_passed}/{total_tests}")
    print(f"Požymiai: {total_features_found}/{total_features}")
    print("=" * 64)

    return files_ok == len(task_names)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def normalize_task_name(name):
    if not name.endswith(".py"):
        name += ".py"
    return name


def parse_cli_args(argv):
    demo_mode = False
    selected_names = []

    for argument in argv:
        if argument in {"-d", "--demo"}:
            demo_mode = True
        elif argument in {"-h", "--help"}:
            checker_name = os.path.basename(__file__)
            print(f"Naudojimas:")
            print(f"  python3 {checker_name}              — visi failai, visi testai")
            print(f"  python3 {checker_name} u1.py        — vienas failas, visi testai")
            print(f"  python3 {checker_name} -d           — visi failai, demo")
            print(f"  python3 {checker_name} -d u1.py     — vienas failas, demo")
            sys.exit(0)
        elif argument.startswith("-"):
            print(f"Nežinomas flag: {argument}")
            sys.exit(1)
        else:
            selected_names.append(normalize_task_name(argument))

    if not selected_names:
        selected_names = list(TASKS.keys())

    unknown = [n for n in selected_names if n not in TASKS]
    if unknown:
        print("Nežinomi failai:")
        for n in unknown:
            print(f"  {n}")
        sys.exit(1)

    unique = []
    for n in selected_names:
        if n not in unique:
            unique.append(n)

    return demo_mode, unique


def main():
    demo_mode, task_names = parse_cli_args(sys.argv[1:])

    if demo_mode:
        run_demo(task_names)
        return

    success = run_full_check(task_names)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
