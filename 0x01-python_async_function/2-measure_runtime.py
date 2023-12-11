#!/usr/bin/env python3
"""
python and async to measure runtime
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time
    Args:
        n: number of coroutines
        max_delay: max delay
    Returns:
        the average delay time in seconds
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
