from functools import lru_cache

from hexatron.const import HEXADECIMALS


@lru_cache()
def _to_hexadecimal(number: int) -> str:
    """
    Recursively convert positive int to hexadecimal string.
    Note: Calling this function with 0 will result in empty string.
    :param number: positive integer
    :return: hexadecimal string
    """
    if number <= 0:
        return ""
    remainder = number % 16
    floor = number // 16
    return _to_hexadecimal(floor) + HEXADECIMALS[remainder]


def to_hexadecimal(number: int) -> str:
    """
    Convert positive or negative integer to hexadecimal string.
    :param number: any integer
    :return: hexadecimal string
    """
    if number == 0:
        return "0"
    return ("" if number > 0 else "-") + _to_hexadecimal(abs(number))
