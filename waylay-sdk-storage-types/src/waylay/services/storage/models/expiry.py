"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class Expiry(WaylayBaseModel):
    """Input model for expiry parameters.."""

    seconds: StrictInt | None = None
    hours: StrictInt | None = None
    days: StrictInt | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
