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

from ..models.notification_queue_status import NotificationQueueStatus


class NotificationQueueStatusReport(WaylayBaseModel):
    """Response model for a notification queue status report.."""

    store: StrictStr
    notification_queues: list[NotificationQueueStatus]
    messages: list[dict[str, Any]] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
