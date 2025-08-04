"""Tests for :mod:`cdr.size_calculator`."""

from __future__ import annotations

from cdr.size_calculator import CdrSizeCalculator


def test_calculates_example_message() -> None:
    """Ensure example tf2_msgs/TFMessage size matches reference."""
    calc = CdrSizeCalculator()

    # geometry_msgs/TransformStamped[] transforms
    calc.sequence_length()
    # std_msgs/Header header
    # time stamp
    calc.uint32()  # uint32 sec
    calc.uint32()  # uint32 nsec
    calc.string(len("base_link"))  # string frame_id
    calc.string(len("radar"))  # string child_frame_id
    # geometry_msgs/Transform transform
    # geometry_msgs/Vector3 translation
    calc.float64()  # float64 x
    calc.float64()  # float64 y
    calc.float64()  # float64 z
    # geometry_msgs/Quaternion rotation
    calc.float64()  # float64 x
    calc.float64()  # float64 y
    calc.float64()  # float64 z
    calc.float64()  # float64 w

    assert calc.size == 100


def test_string_accounts_for_length_and_terminator() -> None:
    calc = CdrSizeCalculator()
    assert calc.size == 4
    assert calc.string(0) == 9  # 4 bytes length + 1 byte terminator
    assert calc.size == 9


def test_sequence_length_alignment() -> None:
    calc = CdrSizeCalculator()
    calc.int8()  # misalign the offset
    assert calc.sequence_length() == 12  # 3 padding bytes + 4 length bytes
