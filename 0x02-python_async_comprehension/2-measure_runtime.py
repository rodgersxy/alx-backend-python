#!/usr/bin/env python3
"""
An asynchronous coroutine that performs a heavy computation.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_computation function
    """
    start = time.time()
    await asyncio.gather(*(
        async_comprehension() for _ in range(4)
    ))
    end = time.time()
    return end - start
