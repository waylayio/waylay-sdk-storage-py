"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.location_inner import LocationInner


class ValidationError(WaylayBaseModel):
    """ValidationError."""

    loc: list[LocationInner]
    msg: StrictStr
    type: StrictStr

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
