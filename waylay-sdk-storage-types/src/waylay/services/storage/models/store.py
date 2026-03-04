"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.links_value import LinksValue
from ..models.storetype import STORETYPE


class Store(WaylayBaseModel):
    """Representation of a backend store.."""

    links: dict[str, LinksValue] | None = Field(default=None, alias="_links")
    type: STORETYPE
    name: StrictStr
    url: StrictStr

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
