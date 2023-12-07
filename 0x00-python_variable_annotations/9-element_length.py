#!/usr/bin/env python3
"""
annonated function's parameters and return values with a
appropriate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return list of tuples
    """
    return [(i, len(i)) for i in lst]
