# coding: utf-8
"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum


from typing_extensions import (
    Self,  # >=3.11
)


class VENTTYPE(str, Enum):
    """Supported notification change event types.."""

    DELETE = "delete"
    PUT = "put"
    GET = "get"

    def __str__(self) -> str:
        return str(self.value)
