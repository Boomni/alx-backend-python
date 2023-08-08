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
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*coroutines)
    return sorted(result)
