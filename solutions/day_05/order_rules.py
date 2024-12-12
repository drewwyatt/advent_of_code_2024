def split_line(line: str) -> tuple[int, int]:
    ints = list(map(int, line.split("|")))
    return ints[0], ints[1]


def get_index(numbers: list[int], value: int) -> int:
    try:
        return numbers.index(value)
    except ValueError:
        return -1


class OrderRules:
    rules: list[tuple[int, int]]

    def __init__(self, input: str) -> None:
        self.rules = list(map(split_line, input.split("\n")))

    def validate(self, page_numbers: list[int]) -> bool:
        for a, b in self.rules:
            first = get_index(page_numbers, a)
            second = get_index(page_numbers, b)
            if first > -1 and second > -1:
                if first > second:
                    return False

        return True
