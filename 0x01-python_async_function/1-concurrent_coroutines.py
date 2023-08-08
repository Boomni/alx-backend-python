#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written and
write an async routine wait_n that takes in 2 int arguments: n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
List of delays should be ascending order without using sort() cause of
concurrency.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawns wait n times with the spacified max_delay"""
    result: list = []
    for x in range(n):
        delay: float = await wait_random(max_delay)
        result.append(delay)
    return result
