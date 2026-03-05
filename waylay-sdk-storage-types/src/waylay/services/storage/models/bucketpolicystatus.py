"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class BUCKETPOLICYSTATUS(str, Enum):
    """Possible bucket policy status codes.."""

    UNKNOWN = "unknown"
    MISSING = "missing"
    OUT_DATED = "out_dated"
    UP_TO_DATE = "up_to_date"

    def __str__(self) -> str:
        return str(self.value)
