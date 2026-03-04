"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class QUEUESETUPSTATUS(str, Enum):
    """Possbile queue setup status codes.."""

    UNKNOWN = "unknown"
    MISSING = "missing"
    INVALID = "invalid"
    NOT_SPECIFIED = "not_specified"
    UP_TO_DATE = "up_to_date"

    def __str__(self) -> str:
        return str(self.value)
