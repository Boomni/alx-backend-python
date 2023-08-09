#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10secs, explain it to yourself.
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures total runtime of executing async_comprehension four times in
    parallel using asyncio.gather

    Return:
        The total runtime measured
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time: float = time.perf_counter()
    total: float = end_time - start_time
    return float(total)
