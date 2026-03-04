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


class HALLink(WaylayBaseModel):
    """Represents a HAL link.."""

    href: StrictStr
    method: StrictStr | None = None
    form_data: dict[str, Any] | None = None
    headers: dict[str, Any] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
