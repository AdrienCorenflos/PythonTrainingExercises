#!/usr/bin/env python
"""Create a generator gen_seq() that creates the infinite geometric series:
1, 1/2, 1/4, 1/8...

Write a function first_N(num) that sums the first num values

Write a function until_small(epsilon) that sums the sequence until the
additional term is less than some small value epsilon.

Created on Sep 21, 2011

@author: paulross
"""

__author__ = 'Adrien Corenflos'

import sys
import pytest


def gen_seq():
    """Generates the infinite geometric series 1, 1/2, 1/4, 1/8, ..."""
    _next = 1
    yield _next
    while True:
        _next /= 2
        yield _next


def first_N(num):
    """Use gen_seq() to generate the sum of the first num values of the series."""
    seq = gen_seq()
    return sum(next(seq) for _ in range(num))


def until_small(epsilon):
    """Use gen_seq() to generate the sum of the series until a value smaller
    than epsilon is encountered."""
    from itertools import takewhile
    seq = gen_seq()
    return sum(takewhile(lambda x: x >= epsilon, seq))


def test_first_N():
    assert 0.0 == first_N(0)
    assert 1.0 == first_N(1)
    assert 1.5 == first_N(2)
    assert 1.75 == first_N(3)
    assert 1.875 == first_N(4)


def test_until_small():
    assert 1.5 == until_small(1.0 / 2)
    assert 1.875 == until_small(1.0 / 8)


def main():
    test_until_small()
    test_first_N()
    return 0


if __name__ == '__main__':
    sys.exit(main())
