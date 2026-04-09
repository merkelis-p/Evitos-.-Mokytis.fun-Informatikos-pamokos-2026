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


class FeatureVisitor(ast.NodeVisitor):
    def __init__(self):
        self.features = set()

    def visit_For(self, node):
        self.features.add("for")
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


def normalize_output(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def parse_int_lines(input_data):
    return [int(line.strip()) for line in input_data.strip().splitlines() if line.strip()]


def reference_nd1(input_data):
    n = parse_int_lines(input_data)[0]
    output = []

    for number in range(1, n + 1):
        if number % 2 == 0 and number % 3 == 0:
            label = "dalijasi_2_ir_3"
        elif number % 2 == 0:
            label = "dalijasi_2"
        elif number % 3 == 0:
            label = "dalijasi_3"
        else:
            label = "nesidalija"

        output.append(f"{number} {label}")

    return "\n".join(output)


def reference_nd2(input_data):
    values = parse_int_lines(input_data)
    n = values[0]
    numbers = values[1:n + 1]

    total = 0
    squares_total = 0
    divisible_by_three = 0

    for number in numbers:
        total += number
        squares_total += number * number
        if number % 3 == 0:
            divisible_by_three += 1

    average = total / n
    return "\n".join(
        [
            f"Suma: {total}",
            f"Kvadratu_suma: {squares_total}",
            f"Dalinasi_is_3: {divisible_by_three}",
            f"Vidurkis: {average:.2f}",
        ]
    )


def reference_nd3(input_data):
    a, b = parse_int_lines(input_data)

    total = 0
    even_total = 0
    divisible_by_3_not_5 = 0
    divisible_by_2_or_7 = 0

    for number in range(a, b + 1):
        total += number

        if number % 2 == 0:
            even_total += number

        if number % 3 == 0 and number % 5 != 0:
            divisible_by_3_not_5 += 1

        if number % 2 == 0 or number % 7 == 0:
            divisible_by_2_or_7 += 1

    return "\n".join(
        [
            f"Suma: {total}",
            f"Lyginiu_suma: {even_total}",
            f"Dalijasi_3_bet_ne_5: {divisible_by_3_not_5}",
            f"Dalijasi_2_arba_7: {divisible_by_2_or_7}",
        ]
    )


def reference_nd4(input_data):
    values = parse_int_lines(input_data)
    n = values[0]
    numbers = values[1:n + 1]

    highest = numbers[0]
    lowest = numbers[0]
    increases = 0
    previous = numbers[0]

    for current in numbers[1:]:
        if current > highest:
            highest = current
        if current < lowest:
            lowest = current
        if current > previous:
            increases += 1
        previous = current

    amplitude = highest - lowest
    return "\n".join(
        [
            f"Didziausias: {highest}",
            f"Maziausias: {lowest}",
            f"Amplitude: {amplitude}",
            f"Padidejimu: {increases}",
        ]
    )


TASKS = {
    "nd1.py": Task(
        file_name="nd1.py",
        title="Dalumo lentelė",
        tests=[
            TestCase(name="Mažas testas", input_data="3\n"),
            TestCase(name="Pavyzdys", input_data="6\n"),
            TestCase(name="Didesnis testas", input_data="8\n"),
        ],
        demo_case=TestCase(name="Demo", input_data="6\n"),
        required_features=["for", "if", "%", "and"],
        reference_solution=reference_nd1,
    ),
    "nd2.py": Task(
        file_name="nd2.py",
        title="Kvadratų statistika",
        tests=[
            TestCase(name="Pavyzdys", input_data="4\n2\n-3\n5\n6\n"),
            TestCase(name="Visi neigiami", input_data="3\n-1\n-2\n-3\n"),
            TestCase(name="Mišrus variantas", input_data="5\n0\n3\n4\n9\n-2\n"),
        ],
        demo_case=TestCase(name="Demo", input_data="4\n2\n-3\n5\n6\n"),
        required_features=["for", "+=", "%", "*", ":.2f"],
        reference_solution=reference_nd2,
    ),
    "nd3.py": Task(
        file_name="nd3.py",
        title="Intervalo analizė",
        tests=[
            TestCase(name="Pavyzdys", input_data="3\n9\n"),
            TestCase(name="Trumpas intervalas", input_data="1\n4\n"),
            TestCase(name="Didesnis intervalas", input_data="10\n18\n"),
        ],
        demo_case=TestCase(name="Demo", input_data="3\n9\n"),
        required_features=["for", "if", "and", "or", "%", "+="],
        reference_solution=reference_nd3,
    ),
    "nd4.py": Task(
        file_name="nd4.py",
        title="Sekos pokyčiai",
        tests=[
            TestCase(name="Pavyzdys", input_data="5\n4\n7\n7\n2\n9\n"),
            TestCase(name="Vienas skaičius", input_data="1\n12\n"),
            TestCase(name="Mišri seka", input_data="6\n5\n3\n8\n8\n10\n1\n"),
        ],
        demo_case=TestCase(name="Demo", input_data="5\n4\n7\n7\n2\n9\n"),
        required_features=["for", "if", ">", "<", "-"],
        reference_solution=reference_nd4,
    ),
}


def inspect_source_code(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        source = file.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        message = f"{error.msg} (eilutė {error.lineno}, stulpelis {error.offset})"
        return set(), message

    visitor = FeatureVisitor()
    visitor.visit(tree)

    if ":.2f" in source:
        visitor.features.add(":.2f")
    if "+=" in source:
        visitor.features.add("+=")
    if "-=" in source:
        visitor.features.add("-=")
    if re.search(r"\belif\b", source):
        visitor.features.add("elif")
    if re.search(r"\belse\s*:", source):
        visitor.features.add("else")

    return visitor.features, None


def progress_bar(done, total, width=20):
    if total == 0:
        return "[--------------------]"
    filled = round((done / total) * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


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
        "kind": "ok" if got == expected else "wrong-answer",
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
    print(f"  Nepraėjęs testas: {test_case.name}")
    if result["kind"] == "wrong-answer":
        difference = first_difference(result["expected"], result["got"])
        if difference is not None:
            line_no, expected_line, got_line = difference
            print(f"  Pirma bloga vieta: eilutė {line_no}")
            print(f"    Laukta: {expected_line}")
            print(f"    Gauta : {got_line}")
    print("  Įvestis:")
    for line in test_case.input_data.strip().splitlines():
        print(f"    {line}")
    print("  Lauktas output:")
    for line in result["expected"].splitlines():
        print(f"    {line}")
    print("  Gautas output:")
    got_text = result["got"] if result["got"] else "(tuščia išvestis)"
    for line in got_text.splitlines():
        print(f"    {line}")


def print_usage():
    checker_name = os.path.basename(__file__)
    print("Naudojimas:")
    print(f"  python3 {checker_name}")
    print(f"  python3 {checker_name} nd1.py")
    print(f"  python3 {checker_name} -d")
    print(f"  python3 {checker_name} -d nd3.py")


def normalize_task_name(argument):
    task_name = os.path.basename(argument)
    if not task_name.endswith(".py"):
        task_name += ".py"
    return task_name


def parse_cli_args(argv):
    demo_mode = False
    selected_names = []

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
            selected_names.append(normalize_task_name(argument))

    if not selected_names:
        selected_names = list(TASKS.keys())

    unknown = [name for name in selected_names if name not in TASKS]
    if unknown:
        print("Nežinomi failai:")
        for name in unknown:
            print(f"  {name}")
        print_usage()
        sys.exit(1)

    unique_names = []
    for name in selected_names:
        if name not in unique_names:
            unique_names.append(name)

    return demo_mode, unique_names


def run_demo(task_names):
    print("=" * 64)
    print("         MATEMATINIU MINI UZDAVINIU DEMO REZIMAS")
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
                difference = first_difference(result["expected"], result["got"])
                if difference is not None:
                    line_no, expected_line, got_line = difference
                    print(f"Pirma bloga vieta: eilutė {line_no}")
                    print(f"Laukta: {expected_line}")
                    print(f"Gauta : {got_line}")
            print("Tikėtinas output:")
            for line in result["expected"].splitlines():
                print(f"  {line}")

        missing_features = [marker for marker in task.required_features if marker not in features]
        if missing_features:
            print(f"Trūkstami požymiai: {' '.join(missing_features)}")

    print("\n" + "=" * 64)


def run_full_check(task_names):
    print("=" * 64)
    print("           MATEMATINIU MINI UZDAVINIU TIKRINTUVAS")
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
            print_failure_details(first_failure[0], first_failure[1])

        found_features = [marker for marker in task.required_features if marker in features]
        missing_features = [marker for marker in task.required_features if marker not in features]
        total_features += len(task.required_features)
        total_features_found += len(found_features)

        print(
            f"Kodo požymiai: {progress_bar(len(found_features), len(task.required_features))} "
            f"{len(found_features)}/{len(task.required_features)}"
        )
        if missing_features:
            print(f"Trūksta: {' '.join(missing_features)}")

        if passed == len(task.tests) and not missing_features:
            files_ok += 1

    print("\nSantrauka:")
    print("-" * 64)
    print(f"Failai be klaidų: {files_ok}/{len(task_names)}")
    print(f"Testai: {total_tests_passed}/{total_tests}")
    print(f"Kodo požymiai: {total_features_found}/{total_features}")
    print("=" * 64)

    return files_ok == len(task_names)


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