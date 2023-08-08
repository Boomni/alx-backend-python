#!/usr/bin/python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    Returns delays in ascending order
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(coroutines):
        results.append(await task)
    return results
