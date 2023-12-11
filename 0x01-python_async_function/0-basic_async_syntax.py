#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    Returns:
        float: the random delay
    """
    delayed = random.uniform(0, max_delay)
    await asyncio.sleep(delayed)
    return delayed
