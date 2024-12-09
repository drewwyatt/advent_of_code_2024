from enum import Enum
from typing import List, Optional


class TrendDirection(Enum):
    Increasing = "increasing"
    Decreasing = "decreasing"


class Report:
    data: list[int]
    trend_direction: Optional[TrendDirection] = None

    def __init__(self, data: list[int]):
        self.data = data

    @staticmethod
    def _parse_line(line: str) -> "Report":
        data = list(map(int, line.strip().split(" ")))  # Convert map to list
        return Report(data)

    @staticmethod
    def from_input(input: str) -> List["Report"]:
        return [Report._parse_line(line) for line in input.strip().split("\n")]

    def get_is_safe(self) -> bool:
        max_index = len(self.data) - 1  # Avoid shadowing built-in max
        for index in range(max_index):
            cur = self.data[index]
            next = self.data[index + 1]
            if not (
                self._has_consistent_trend_direction(cur, next)
                and self._has_appropriate_level_difference(cur, next)
            ):
                return False
        return True

    def _has_consistent_trend_direction(self, cur: int, next: int) -> bool:
        self.trend_direction = self.trend_direction or self._get_trend_direction(
            cur, next
        )
        return self.trend_direction == self._get_trend_direction(cur, next)

    def _has_appropriate_level_difference(self, cur: int, next: int) -> bool:
        diff = abs(cur - next)
        return 1 <= diff <= 3  # Simplified range check

    def _get_trend_direction(self, cur: int, next: int) -> TrendDirection:
        return TrendDirection.Increasing if next > cur else TrendDirection.Decreasing
