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

from ..models.s3_policy_statement import S3PolicyStatement


class S3PolicyDef(WaylayBaseModel):
    """AWS S3 Policy definition.."""

    statement: list[S3PolicyStatement] | None = Field(
        default=None, alias="Statement"
    )
    version: StrictStr | None = Field(default=None, alias="Version")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
