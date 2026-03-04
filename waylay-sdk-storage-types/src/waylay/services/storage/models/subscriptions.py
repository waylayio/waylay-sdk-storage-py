"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.bucket import Bucket
from ..models.links_value import LinksValue
from ..models.subscription_config_output import SubscriptionConfigOutput


class Subscriptions(WaylayBaseModel):
    """Listing object for subscriptions.."""

    links: dict[str, LinksValue] | None = Field(default=None, alias="_links")
    bucket: Bucket
    subscriptions: list[SubscriptionConfigOutput]
    warnings: list[dict[str, Any]] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
