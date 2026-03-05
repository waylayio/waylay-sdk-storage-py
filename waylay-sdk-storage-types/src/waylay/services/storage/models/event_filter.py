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

from ..models.eventtype import EVENTTYPE


class EventFilter(WaylayBaseModel):
    """Filter on change events in a storage backend.  The `prefix` and `suffix` properties are conditions on the object path (not including the bucket name). When not specified, all paths in the bucket will selected.  The `events` property can contain `put` and/or `delete` values, corresponding to create/update and deletion events. When not specified, only the create/update events are filtered.."""

    prefix: StrictStr | None = None
    suffix: StrictStr | None = None
    events: list[EVENTTYPE] | None = None
    description: StrictStr | None = None
    queue: StrictStr | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
