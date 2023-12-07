#!/usr/bin/env python3
"""
iterable object TypeVar
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The input dictionary.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key if found,
        or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
