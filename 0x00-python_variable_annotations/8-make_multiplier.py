#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier.
    """
    def f(num: float) -> float:
        """ multiplies a float by multiplier """
        return num * multiplier

    return f
