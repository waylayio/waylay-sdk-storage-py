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

from ..models.auth import AUTH


class AuthenticationConfig(WaylayBaseModel):
    """Authentication configuration when forwarding an event to a channel.."""

    method: AUTH | None = None
    key: StrictStr | None = None
    secret: StrictStr | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
