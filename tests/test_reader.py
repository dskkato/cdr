from __future__ import annotations

import pytest

from cdr.encapsulation_kind import EncapsulationKind
from cdr.reader import CdrReader

TF2_MSG_TFMESSAGE = (
    "0001000001000000cce0d158f08cf9060a000000626173655f6c696e6b0000000600000072616461"
    "72000000ae47e17a14ae0e4000000000000000000000000000000000000000000000000000000000"
    "000000000000000000000000000000000000f03f"
)


def test_parses_example_tf2_message() -> None:
    data = bytes.fromhex(TF2_MSG_TFMESSAGE)
    reader = CdrReader(data)
    assert reader.decoded_bytes == 4

    # geometry_msgs/TransformStamped[] transforms
    assert reader.sequence_length() == 1
    # std_msgs/Header header
    # time stamp
    assert reader.uint32() == 1490149580  # uint32 sec
    assert reader.uint32() == 117017840  # uint32 nsec
    assert reader.string() == "base_link"  # string frame_id
    assert reader.string() == "radar"  # string child_frame_id
    # geometry_msgs/Transform transform
    # geometry_msgs/Vector3 translation
    assert reader.float64() == pytest.approx(3.835)  # float64 x
    assert reader.float64() == pytest.approx(0)  # float64 y
    assert reader.float64() == pytest.approx(0)  # float64 z
    # geometry_msgs/Quaternion rotation
    assert reader.float64() == pytest.approx(0)  # float64 x
    assert reader.float64() == pytest.approx(0)  # float64 y
    assert reader.float64() == pytest.approx(0)  # float64 z
    assert reader.float64() == pytest.approx(1)  # float64 w

    assert reader.offset == len(data)
    assert reader.kind == EncapsulationKind.CDR_LE
    assert reader.decoded_bytes == len(data)
    assert reader.byte_length == len(data)
