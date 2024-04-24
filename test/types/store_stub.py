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
    from waylay.services.storage.models.store import Store

    StoreAdapter = TypeAdapter(Store)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

store_model_schema = json.loads(
    r"""{
  "title" : "Store",
  "required" : [ "name", "type", "url" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : " Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/_Links"
      }
    },
    "type" : {
      "$ref" : "#/components/schemas/STORE_TYPE"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "url" : {
      "title" : "Url",
      "type" : "string"
    }
  },
  "description" : "Representation of a backend store."
}
""",
    object_hook=with_example_provider,
)
store_model_schema.update({"definitions": MODEL_DEFINITIONS})

store_faker = JSF(store_model_schema, allow_none_optionals=1)


class StoreStub:
    """Store unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return store_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Store":
        """Create Store stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(StoreAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return StoreAdapter.validate_python(json, context={"skip_validation": True})
