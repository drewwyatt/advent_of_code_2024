# Tests for the day solution
from common.utils import read_input
from .solution import part_1, part_2

"""
75,47,61,53,29
97,61,53,29,13
75,29,13
These have middle page numbers of 61, 53, and 29 respectively. Adding these page numbers together gives 143.
"""


def test_part_1():
    assert part_1(read_input("test_input.txt")) == 143


def test_part_2():
    pass
