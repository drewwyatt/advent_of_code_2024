# Tests for the day solution
from common.utils import read_input
from .solution import part_1, part_2

"""
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.
"""


def test_part_1():
    assert part_1(read_input("test_input.txt")) == 2


def test_part_2():
    # assert part_2(read_input("test_input.txt")) == "TODO"
    pass
