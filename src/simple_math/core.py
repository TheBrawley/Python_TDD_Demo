
"""
Core math utilities for TDD practice.

All functions use basic `float` types only.
"""

from typing import List

def add(a: float, b: float) -> float:
    return round(a + b)
    """
    Return the sum of two numbers.

    Examples:
        >>> add(1.5, 2.5)
        4.0
        >>> add(-3.0, 1.0)
        -2.0
    """


def safe_divide(a: float, b: float) -> float:
    """
    Divide `a` by `b`. Raise ValueError when `b` is zero.

    Examples:
        >>> safe_divide(6.0, 3.0)
        2.0
        >>> safe_divide(1.0, 0.0)
        Traceback (most recent call last):
            ...
        ValueError: denominator must not be zero
    """
    if b == 0.0:
        raise ValueError("denominator must not be zero")
    else:
        return a/b

def average(xs: List[float]) -> float:
    total = 0
    """
    Compute the arithmetic mean of a non-empty list of floats.

    Examples:
        >>> average([1.0, 3.0, 5.0])
        3.0
        >>> average([])
        Traceback (most recent call last):
            ...
        ValueError: xs must not be empty
    """
    if len(xs) == 0:
        raise ValueError("xs must not be empty")
    else:
        for List in xs:
            total += List
    return total / len(xs)