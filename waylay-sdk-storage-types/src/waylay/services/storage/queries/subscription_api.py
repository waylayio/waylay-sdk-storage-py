# coding: utf-8
"""Waylay Storage query parameters.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from pydantic import (
    ConfigDict,
    StrictInt,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.channeltype import CHANNELTYPE
from ..models.venttype import VENTTYPE


def _create_query_alias_for(field_name: str) -> str:
    if field_name == "store":
        return "store"
    return field_name


class CreateQuery(WaylayBaseModel):
    """Model for `create` query parameters."""

    store: StrictStr | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_create_query_alias_for,
        populate_by_name=True,
    )


def _delete_by_query_alias_for(field_name: str) -> str:
    if field_name == "start_after":
        return "start_after"
    if field_name == "prefix":
        return "prefix"
    if field_name == "suffix":
        return "suffix"
    if field_name == "event_type":
        return "event_type"
    if field_name == "channel_type":
        return "channel_type"
    if field_name == "channel_id":
        return "channel_id"
    if field_name == "store":
        return "store"
    if field_name == "max_keys":
        return "max_keys"
    return field_name


class DeleteByQuery(WaylayBaseModel):
    """Model for `delete_by` query parameters."""

    start_after: StrictStr | None = None
    prefix: StrictStr | None = None
    suffix: StrictStr | None = None
    event_type: VENTTYPE | None = None
    channel_type: CHANNELTYPE | None = None
    channel_id: StrictStr | None = None
    store: StrictStr | None = None
    max_keys: StrictInt | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_delete_by_query_alias_for,
        populate_by_name=True,
    )


def _get_query_alias_for(field_name: str) -> str:
    if field_name == "store":
        return "store"
    return field_name


class GetQuery(WaylayBaseModel):
    """Model for `get` query parameters."""

    store: StrictStr | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_query_alias_for,
        populate_by_name=True,
    )


def _list_query_alias_for(field_name: str) -> str:
    if field_name == "store":
        return "store"
    if field_name == "prefix":
        return "prefix"
    if field_name == "suffix":
        return "suffix"
    if field_name == "event_type":
        return "event_type"
    if field_name == "channel_type":
        return "channel_type"
    if field_name == "channel_id":
        return "channel_id"
    if field_name == "max_keys":
        return "max_keys"
    return field_name


class ListQuery(WaylayBaseModel):
    """Model for `list` query parameters."""

    store: StrictStr | None = None
    prefix: StrictStr | None = None
    suffix: StrictStr | None = None
    event_type: VENTTYPE | None = None
    channel_type: CHANNELTYPE | None = None
    channel_id: StrictStr | None = None
    max_keys: StrictInt | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_query_alias_for,
        populate_by_name=True,
    )


def _query_query_alias_for(field_name: str) -> str:
    if field_name == "start_after":
        return "start_after"
    if field_name == "store":
        return "store"
    if field_name == "prefix":
        return "prefix"
    if field_name == "suffix":
        return "suffix"
    if field_name == "event_type":
        return "event_type"
    if field_name == "channel_type":
        return "channel_type"
    if field_name == "channel_id":
        return "channel_id"
    if field_name == "max_keys":
        return "max_keys"
    return field_name


class QueryQuery(WaylayBaseModel):
    """Model for `query` query parameters."""

    start_after: StrictStr | None = None
    store: StrictStr | None = None
    prefix: StrictStr | None = None
    suffix: StrictStr | None = None
    event_type: VENTTYPE | None = None
    channel_type: CHANNELTYPE | None = None
    channel_id: StrictStr | None = None
    max_keys: StrictInt | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_query_query_alias_for,
        populate_by_name=True,
    )


def _remove_query_alias_for(field_name: str) -> str:
    if field_name == "store":
        return "store"
    return field_name


class RemoveQuery(WaylayBaseModel):
    """Model for `remove` query parameters."""

    store: StrictStr | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_remove_query_alias_for,
        populate_by_name=True,
    )


def _replace_query_alias_for(field_name: str) -> str:
    if field_name == "store":
        return "store"
    return field_name


class ReplaceQuery(WaylayBaseModel):
    """Model for `replace` query parameters."""

    store: StrictStr | None = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_replace_query_alias_for,
        populate_by_name=True,
    )
