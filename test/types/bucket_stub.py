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
    from waylay.services.storage.models.bucket import Bucket

    BucketAdapter = TypeAdapter(Bucket)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

bucket_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : " Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/_Links_value"
      }
    },
    "alias" : {
      "title" : "Alias",
      "type" : "string"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "store" : {
      "$ref" : "#/components/schemas/Store"
    },
    "creation_date" : {
      "title" : "Creation Date",
      "type" : "string",
      "format" : "date-time"
    },
    "size" : {
      "title" : "Size",
      "type" : "integer"
    }
  },
  "description" : "Representation of a storage bucket."
}
""",
    object_hook=with_example_provider,
)
bucket_model_schema.update({"definitions": MODEL_DEFINITIONS})

bucket_faker = JSF(bucket_model_schema, allow_none_optionals=1)


class BucketStub:
    """Bucket unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return bucket_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Bucket":
        """Create Bucket stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(BucketAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BucketAdapter.validate_python(json, context={"skip_validation": True})
