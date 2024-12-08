from common.utils import read_input


def parse_input(input: str):
    left_column: list[int] = []
    right_column: list[int] = []

    for line in input.strip().split("\n"):
        left, right = map(int, line.split())
        left_column.append(left)
        right_column.append(right)

    left_column.sort()
    right_column.sort()

    return left_column, right_column


def get_difference(left: int, right: int):
    return left - right if left > right else right - left


def part_1(input: str):
    left_column, right_column = parse_input(input)
    difference = 0

    for index in range(len(left_column)):
        left = left_column[index]
        right = right_column[index]
        difference += get_difference(left, right)

    return difference


def part_2(input: str):
    pass


def solve(input: str, part: int):
    return part_1(input) if part == 1 else part_2(input)
