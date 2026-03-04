"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class CHANNELTYPE(str, Enum):
    """Supported notification channel types.."""

    WEBHOOK = "webhook"
    WEBSCRIPT = "webscript"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
