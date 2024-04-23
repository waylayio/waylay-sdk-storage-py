# coding: utf-8
"""Waylay Storage query parameters.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from pydantic import (
    ConfigDict,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


def _status_query_alias_for(field_name: str) -> str:
    if field_name == "store":
        return "store"
    if field_name == "include_buckets":
        return "include_buckets"
    if field_name == "include_queues":
        return "include_queues"
    if field_name == "include_disk_usage":
        return "include_disk_usage"
    return field_name


class StatusQuery(WaylayBaseModel):
    """Model for `status` query parameters."""

    store: StrictStr | None = None
    include_buckets: StrictBool | None = None
    include_queues: StrictBool | None = None
    include_disk_usage: StrictBool | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_status_query_alias_for,
        populate_by_name=True,
    )


def _version_query_alias_for(field_name: str) -> str:
    return field_name


class VersionQuery(WaylayBaseModel):
    """Model for `version` query parameters."""

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_version_query_alias_for,
        populate_by_name=True,
    )
