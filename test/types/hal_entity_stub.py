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
    from waylay.services.storage.models.hal_entity import HALEntity

    HALEntityAdapter = TypeAdapter(HALEntity)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

hal_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : " Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/_Links"
      }
    }
  },
  "description" : "Output model representing a collection of HAL links."
}
""",
    object_hook=with_example_provider,
)
hal_entity_model_schema.update({"definitions": MODEL_DEFINITIONS})

hal_entity_faker = JSF(hal_entity_model_schema, allow_none_optionals=1)


class HALEntityStub:
    """HALEntity unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return hal_entity_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "HALEntity":
        """Create HALEntity stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(HALEntityAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return HALEntityAdapter.validate_python(json, context={"skip_validation": True})
