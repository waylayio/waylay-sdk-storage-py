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
    from waylay.services.storage.models.expiry import Expiry

    ExpiryAdapter = TypeAdapter(Expiry)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

expiry_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "seconds" : {
      "title" : "Seconds",
      "type" : "integer"
    },
    "hours" : {
      "title" : "Hours",
      "type" : "integer"
    },
    "days" : {
      "title" : "Days",
      "type" : "integer"
    }
  },
  "description" : "Input model for expiry parameters."
}
""",
    object_hook=with_example_provider,
)
expiry_model_schema.update({"definitions": MODEL_DEFINITIONS})

expiry_faker = JSF(expiry_model_schema, allow_none_optionals=1)


class ExpiryStub:
    """Expiry unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return expiry_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Expiry":
        """Create Expiry stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(ExpiryAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExpiryAdapter.validate_python(json, context={"skip_validation": True})
