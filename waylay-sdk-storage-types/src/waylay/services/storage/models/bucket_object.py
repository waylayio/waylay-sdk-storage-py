"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.bucket import Bucket
from ..models.links_value import LinksValue


class BucketObject(WaylayBaseModel):
    """Representation of a storage object.."""

    links: dict[str, LinksValue] | None = Field(default=None, alias="_links")
    bucket: Bucket
    name: StrictStr
    last_modified: datetime | None = None
    etag: StrictStr | None = None
    size: StrictInt | None = None
    content_type: StrictStr | None = None
    is_dir: StrictBool | None = False
    storage_class: StrictStr | None = None
    owner_id: StrictStr | None = None
    owner_name: StrictStr | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
