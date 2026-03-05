"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.bucket_configuration import BucketConfiguration
from ..models.bucketcreationstatus import BUCKETCREATIONSTATUS
from ..models.bucketpolicystatus import BUCKETPOLICYSTATUS
from ..models.notification_queue_status_report import NotificationQueueStatusReport
from ..models.queuesetupstatus import QUEUESETUPSTATUS


class TenantStatusReport(WaylayBaseModel):
    """Response model for a tenant status report.."""

    tenant: StrictStr
    buckets: list[BucketConfiguration] | None = None
    queues: list[NotificationQueueStatusReport] | None = None
    total_size: StrictInt | None = None
    bucket_status: BUCKETCREATIONSTATUS | None = None
    policy_status: BUCKETPOLICYSTATUS | None = None
    queue_status: QUEUESETUPSTATUS | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
