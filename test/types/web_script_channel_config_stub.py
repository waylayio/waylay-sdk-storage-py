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
    from waylay.services.storage.models.web_script_channel_config import (
        WebScriptChannelConfig,
    )

    WebScriptChannelConfigAdapter = TypeAdapter(WebScriptChannelConfig)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

web_script_channel_config_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/WebScriptChannelConfig_type"
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
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "version" : {
      "title" : "Version",
      "type" : "string"
    },
    "method" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/HTTP_METHOD"
      } ],
      "default" : "POST"
    }
  },
  "description" : "Channel configuration for invoking a waylay webscript."
}
""",
    object_hook=with_example_provider,
)
web_script_channel_config_model_schema.update({"definitions": MODEL_DEFINITIONS})

web_script_channel_config_faker = JSF(
    web_script_channel_config_model_schema, allow_none_optionals=1
)


class WebScriptChannelConfigStub:
    """WebScriptChannelConfig unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return web_script_channel_config_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "WebScriptChannelConfig":
        """Create WebScriptChannelConfig stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                WebScriptChannelConfigAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return WebScriptChannelConfigAdapter.validate_python(
            json, context={"skip_validation": True}
        )
