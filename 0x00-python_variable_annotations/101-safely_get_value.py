#!/usr/bin/env python3
"""
iterable object TypeVar
"""
from typing import Any, Union, Mapping, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns:
        Union[T, None]: The value associated with the key if found,
        or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
