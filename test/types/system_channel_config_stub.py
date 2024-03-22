# coding: utf-8
"""Waylay Storage model tests.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.storage.models.system_channel_config import SystemChannelConfig

    SystemChannelConfigAdapter = TypeAdapter(SystemChannelConfig)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

system_channel_config_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "Type",
      "type" : "string",
      "default" : "system",
      "enum" : [ "system" ]
    },
    "description" : {
      "title" : "Description",
      "type" : "string"
    },
    "payload" : {
      "$ref" : "#/components/schemas/PayloadConfig"
    },
    "authentication" : {
      "$ref" : "#/components/schemas/AuthenticationConfig"
    },
    "expiry" : {
      "$ref" : "#/components/schemas/Expiry"
    }
  },
  "description" : "Channel configuration for functionality that is fixed by the platform.\n\nThis cannot be selected by the end user."
}
""",
    object_hook=with_example_provider,
)
system_channel_config_model_schema.update({"definitions": MODEL_DEFINITIONS})

system_channel_config_faker = JSF(
    system_channel_config_model_schema, allow_none_optionals=1
)


class SystemChannelConfigStub:
    """SystemChannelConfig unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return system_channel_config_faker.generate()

    @classmethod
    def create_instance(cls) -> "SystemChannelConfig":
        """Create SystemChannelConfig stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SystemChannelConfigAdapter.validate_python(cls.create_json())
