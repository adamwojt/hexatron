"""Tests for `hexatron` package."""

import pytest

from hexatron.hexatron import to_hexadecimal


@pytest.mark.parametrize(
    "test_case, expected_hexadecimal_string",
    [
        (0, "0"),
        (-1, "-1"),
        (-0, "0"),
        (21, "15"),
        (666, "29A"),
        (2021, "7E5"),
        (3223, "C97"),
        (64356, "FB64"),
    ],
)
def test_to_hexadecimal(test_case, expected_hexadecimal_string):
    assert to_hexadecimal(test_case) == expected_hexadecimal_string
