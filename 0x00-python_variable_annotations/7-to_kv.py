#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert string-key & int/float-value to tuple with square of value as float
    """
    return (k, v**2)
