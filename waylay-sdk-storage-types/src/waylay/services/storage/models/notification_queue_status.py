"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

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
    configured_parameters: dict[str, Any] | None = None
    actual_parameters: dict[str, Any] | None = None
    error: StrictStr | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
