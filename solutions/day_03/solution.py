import re

pattern = re.compile(r"mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)")


def part_1(input: str):
    sum = 0
    matches = pattern.findall(input)
    for a, b in matches:
        sum += int(a) * int(b)

    return sum


def remove_donts(chunk: str, chunk_index: int) -> str:
    do_index = chunk.find("do")
    if do_index != -1:
        return chunk[do_index + 2 :]
    else:
        return chunk if chunk_index == 0 else ""


def part_2(input: str):
    scrubbed = ""
    for index, chunk in enumerate(input.split("don't")):
        scrubbed += remove_donts(chunk, index)

    return part_1(scrubbed)


def solve(input: str, part: int):
    return part_1(input) if part == 1 else part_2(input)
