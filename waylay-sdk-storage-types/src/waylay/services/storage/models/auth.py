# coding: utf-8
"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AUTH(str, Enum):
    """Supported authentication methods for notifications.."""

    DEFAULT = "DEFAULT"
    NONE = "NONE"
    API_KEY = "API_KEY"
    TOKEN = "TOKEN"
    WAYLAY_APP = "WAYLAY_APP"
    WAYLAY_TOKEN = "WAYLAY_TOKEN"
    WEBSCRIPT = "WEBSCRIPT"

    def __str__(self) -> str:
        return str(self.value)