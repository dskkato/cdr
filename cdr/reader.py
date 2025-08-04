"""Placeholder for the :class:`CdrReader` implementation.

The original TypeScript project exposes a ``CdrReader`` class capable of
parsing CDR encoded byte streams.  A full port of that functionality is
outside the scope of this exercise; however, providing a minimal stub
allows other modules to import :class:`CdrReader` without failing.
"""

from __future__ import annotations


class CdrReader:
    """Stub implementation that raises ``NotImplementedError`` on use."""

    def __init__(self, *args, **kwargs) -> None:  # noqa: D401 - simple stub
        raise NotImplementedError("CdrReader is not yet implemented")
