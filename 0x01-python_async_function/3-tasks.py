#!/usr/bin/env python3
"""
async asyncio tasks
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    creates and returns a task that waits for a random delay
    Args:
        max_delay: max delay in seconds
    Returns:
        task
    """

    return asyncio.create_task(wait_random(max_delay))
