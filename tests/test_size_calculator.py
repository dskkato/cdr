"""Tests for :mod:`cdr.size_calculator`."""

from __future__ import annotations

from cdr.size_calculator import CdrSizeCalculator


def test_string_accounts_for_length_and_terminator() -> None:
    calc = CdrSizeCalculator()
    assert calc.size == 4
    assert calc.string(0) == 9  # 4 bytes length + 1 byte terminator
    assert calc.size == 9


def test_sequence_length_alignment() -> None:
    calc = CdrSizeCalculator()
    calc.int8()  # misalign the offset
    assert calc.sequence_length() == 12  # 3 padding bytes + 4 length bytes

