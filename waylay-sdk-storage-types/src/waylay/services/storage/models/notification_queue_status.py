# coding: utf-8
"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict

from pydantic import (
    ConfigDict,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.queuesetupstatus import QUEUESETUPSTATUS


class NotificationQueueStatus(WaylayBaseModel):
    """Response model for the notification queue configuration.."""

    status: QUEUESETUPSTATUS
    name: StrictStr
    method: StrictStr
    configured_parameters: Dict[str, Any] | None = None
    actual_parameters: Dict[str, Any] | None = None
    error: StrictStr | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
