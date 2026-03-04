"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class STORETYPE(str, Enum):
    """Supported backend store types.."""

    GS = "gs"
    S3 = "s3"
    AZURE = "azure"
    ZENKO = "zenko"

    def __str__(self) -> str:
        return str(self.value)
