#!/usr/bin/python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """Spawns wait n times with the spacified max_delay"""
    result: list = []
    for x in range(n):
        delay: float = await task_wait_random(max_delay)
        result.append(delay)
    return result

