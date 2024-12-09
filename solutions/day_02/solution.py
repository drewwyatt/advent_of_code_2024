from .report import Report


def part_1(input: str):
    reports = Report.from_input(input)
    safe_reports = 0
    for report in reports:
        if report.get_is_safe():
            safe_reports += 1

    return safe_reports


def part_2(input: str):
    pass


def solve(input: str, part: int):
    return part_1(input) if part == 1 else part_2(input)
