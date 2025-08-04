from __future__ import annotations

import pytest

from cdr.encapsulation_kind import EncapsulationKind
from cdr.writer import CdrWriter

TF2_MSG_TFMESSAGE = (
    "0001000001000000cce0d158f08cf9060a000000626173655f6c696e6b0000000600000072616461"
    "72000000ae47e17a14ae0e4000000000000000000000000000000000000000000000000000000000"
    "000000000000000000000000000000000000f03f"
)


def write_example_message(writer: CdrWriter) -> None:
    # geometry_msgs/TransformStamped[] transforms
    writer.sequenceLength(1)
    # std_msgs/Header header
    # time stamp
    writer.uint32(1490149580)  # uint32 sec
    writer.uint32(117017840)  # uint32 nsec
    writer.string("base_link")  # string frame_id
    writer.string("radar")  # string child_frame_id
    # geometry_msgs/Transform transform
    # geometry_msgs/Vector3 translation
    writer.float64(3.835)  # float64 x
    writer.float64(0)  # float64 y
    writer.float64(0)  # float64 z
    # geometry_msgs/Quaternion rotation
    writer.float64(0)  # float64 x
    writer.float64(0)  # float64 y
    writer.float64(0)  # float64 z
    writer.float64(1)  # float64 w


@pytest.mark.parametrize("kwargs", [{"size": 100}, {"buffer": bytearray(100)}])
@pytest.mark.parametrize("kind", [EncapsulationKind.CDR_LE, EncapsulationKind.CDR2_LE])
def test_serializes_example_message_with_preallocation(
    kind: EncapsulationKind,
    kwargs: dict,
) -> None:
    writer = CdrWriter(kind=kind, **kwargs)
    write_example_message(writer)
    assert writer.size == 100
    expected = bytearray.fromhex(TF2_MSG_TFMESSAGE)
    expected[1] = kind.value
    assert writer.data == bytes(expected)


def test_serializes_example_message_without_preallocation() -> None:
    writer = CdrWriter()
    write_example_message(writer)
    assert writer.size == 100
    assert writer.data.hex() == TF2_MSG_TFMESSAGE
