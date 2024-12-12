import re

pattern = re.compile(r"mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)")


def part_1(input: str):
    sum = 0
    matches = pattern.findall(input)
    for a, b in matches:
        sum += int(a) * int(b)

    return sum


def part_2(input: str):
    pass


def solve(input: str, part: int):
    return part_1(input) if part == 1 else part_2(input)
