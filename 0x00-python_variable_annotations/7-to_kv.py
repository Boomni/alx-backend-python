#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string-key and int/float-value pair to a tuple with the square of the value as a float.

    Parameters:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string key and the square of the value as a float.
    """
    return (k, v**2)
