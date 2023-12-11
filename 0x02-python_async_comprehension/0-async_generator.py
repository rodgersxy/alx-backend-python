#!/usr/bin/env python3
"""
Asynchrounous generator that takes no arguments
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that takes no arguments
    Yields:
        float: random float
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
