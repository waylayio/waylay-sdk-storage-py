# coding: utf-8
"""Waylay Storage model tests.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.storage.models.system_channel_config_type import (
        SystemChannelConfigType,
    )

    SystemChannelConfigTypeAdapter = TypeAdapter(SystemChannelConfigType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

system_channel_config_type_model_schema = json.loads(
    r"""{
  "title" : "SystemChannelConfig_type",
  "type" : "string",
  "default" : "system",
  "enum" : [ "system" ]
}
""",
    object_hook=with_example_provider,
)
system_channel_config_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

system_channel_config_type_faker = JSF(
    system_channel_config_type_model_schema, allow_none_optionals=1
)


class SystemChannelConfigTypeStub:
    """SystemChannelConfigType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return system_channel_config_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "SystemChannelConfigType":
        """Create SystemChannelConfigType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SystemChannelConfigTypeAdapter.validate_python(cls.create_json())
