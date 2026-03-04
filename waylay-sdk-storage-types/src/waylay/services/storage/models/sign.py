"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class SIGN(str, Enum):
    """Supported `sign` url parameter values.."""

    GET = "GET"
    PUT = "PUT"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
