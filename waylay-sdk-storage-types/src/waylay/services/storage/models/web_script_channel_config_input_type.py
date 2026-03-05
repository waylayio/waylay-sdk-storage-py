"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class WebScriptChannelConfigInputType(str, Enum):
    """WebScriptChannelConfigInputType."""

    WEBSCRIPT = "webscript"

    def __str__(self) -> str:
        return str(self.value)
