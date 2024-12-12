from .order_rules import OrderRules


def to_page_numbers(line: str) -> list[int]:
    return list(map(int, line.split(",")))


def parse_input(input: str) -> tuple[OrderRules, list[list[int]]]:
    rules_section, pages_section = input.split("\n\n")
    pages = list(map(to_page_numbers, pages_section.split("\n")))
    return OrderRules(rules_section), pages


def get_middle_number(numbers: list[int]) -> int:
    index = round((len(numbers) - 1) / 2)
    return numbers[index]


def part_1(input: str) -> int:
    sum = 0
    rules, page_numbers = parse_input(input)
    for pages in page_numbers:
        if rules.validate(pages):
            sum += get_middle_number(pages)

    return sum


def part_2(input: str):
    pass


def solve(input: str, part: int):
    return part_1(input) if part == 1 else part_2(input)
