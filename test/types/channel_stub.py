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
    from waylay.services.storage.models.channel import Channel

    ChannelAdapter = TypeAdapter(Channel)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

channel_model_schema = json.loads(
    r"""{
  "title" : "Channel",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/WebScriptChannelConfig"
  }, {
    "$ref" : "#/components/schemas/SystemChannelConfig"
  } ]
}
""",
    object_hook=with_example_provider,
)
channel_model_schema.update({"definitions": MODEL_DEFINITIONS})

channel_faker = JSF(channel_model_schema, allow_none_optionals=1)


class ChannelStub:
    """Channel unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return channel_faker.generate()

    @classmethod
    def create_instance(cls) -> "Channel":
        """Create Channel stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ChannelAdapter.validate_python(cls.create_json())