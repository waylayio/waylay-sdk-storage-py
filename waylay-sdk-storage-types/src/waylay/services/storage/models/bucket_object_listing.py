"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.bucket_object import BucketObject
from ..models.links_value import LinksValue


class BucketObjectListing(WaylayBaseModel):
    """List of storage object representations.."""

    links: dict[str, LinksValue] | None = Field(default=None, alias="_links")
    objects: list[BucketObject]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
