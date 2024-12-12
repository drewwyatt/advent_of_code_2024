# Tests for the day solution
from common.utils import read_input
from .solution import part_1, part_2

"""
For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

"""


def test_part_1():
    assert part_1(read_input("test_input.txt")) == 161


def test_part_2():
    pass
    # assert part_2(read_input("test_input.txt")) == "TODO"
