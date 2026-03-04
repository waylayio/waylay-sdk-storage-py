"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class EVENTTYPE(str, Enum):
    """Supported notification change event types.."""

    DELETE = "delete"
    PUT = "put"
    GET = "get"

    def __str__(self) -> str:
        return str(self.value)
