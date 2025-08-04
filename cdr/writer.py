"""Placeholder for the :class:`CdrWriter` implementation.

A full featured writer is not required for the initial port but the class
is defined so that importing it from the package succeeds.
"""

from __future__ import annotations


class CdrWriter:
    """Stub implementation that raises ``NotImplementedError`` on use."""

    def __init__(self, *args, **kwargs) -> None:  # noqa: D401 - simple stub
        raise NotImplementedError("CdrWriter is not yet implemented")
