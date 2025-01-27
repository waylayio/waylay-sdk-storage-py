# coding: utf-8
"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import (
    ConfigDict,
    Field,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.bucket import Bucket
from ..models.links_value import LinksValue
from ..models.subscription_config import SubscriptionConfig


class Subscriptions(WaylayBaseModel):
    """Listing object for subscriptions.."""

    links: Dict[str, LinksValue] | None = Field(default=None, alias="_links")
    bucket: Bucket
    subscriptions: List[SubscriptionConfig]
    warnings: List[Dict[str, Any]] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
