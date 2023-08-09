#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[int, None, None]:
    """
    Loops 10 times
    In each loop asynchroniously waits 1sec & yields random number btw 0 - 10
    I used Generator as return type cos i got to learn you need to use:
        Iterable: When function returns an object that can be iterated over.
        Iterator: Return an iterator, without specifying what type of iterator.
        Generator: to explicitly convey that a function returns a generator
                    & possibly specify the types of values that can be sent to
                    or returned from the generator.

        Iterable
        Generator
        Iterator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
