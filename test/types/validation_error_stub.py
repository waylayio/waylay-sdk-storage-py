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
    from waylay.services.storage.models.validation_error import ValidationError

    ValidationErrorAdapter = TypeAdapter(ValidationError)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

validation_error_model_schema = json.loads(
    r"""{
  "title" : "ValidationError",
  "required" : [ "loc", "msg", "type" ],
  "type" : "object",
  "properties" : {
    "loc" : {
      "title" : "Location",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Location_inner"
      }
    },
    "msg" : {
      "title" : "Message",
      "type" : "string"
    },
    "type" : {
      "title" : "Error Type",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
validation_error_model_schema.update({"definitions": MODEL_DEFINITIONS})

validation_error_faker = JSF(validation_error_model_schema, allow_none_optionals=1)


class ValidationErrorStub:
    """ValidationError unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return validation_error_faker.generate()

    @classmethod
    def create_instance(cls) -> "ValidationError":
        """Create ValidationError stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ValidationErrorAdapter.validate_python(cls.create_json())
