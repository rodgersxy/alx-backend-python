#!/usr/bin/env python3
"""
python async_comprehension.py
"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    returns list of 10 random numbers
    """
    return [i async for i in async_generator()]
