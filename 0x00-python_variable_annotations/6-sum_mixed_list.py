#!/usr/bin/env python3

""" mixed list """
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of integers and floats in the mixed list.

    Parameters:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of the integers and floats in the list as a float.
    """
    return float(sum(mxd_lst))
