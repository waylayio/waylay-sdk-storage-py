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
    from waylay.services.storage.models.subscriptions import Subscriptions

    SubscriptionsAdapter = TypeAdapter(Subscriptions)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

subscriptions_model_schema = json.loads(
    r"""{
  "required" : [ "bucket", "subscriptions" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : " Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/_Links"
      }
    },
    "bucket" : {
      "$ref" : "#/components/schemas/Bucket"
    },
    "subscriptions" : {
      "title" : "Subscriptions",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/SubscriptionConfig"
      }
    },
    "warnings" : {
      "title" : "Warnings",
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    }
  },
  "description" : "Listing object for subscriptions."
}
""",
    object_hook=with_example_provider,
)
subscriptions_model_schema.update({"definitions": MODEL_DEFINITIONS})

subscriptions_faker = JSF(subscriptions_model_schema, allow_none_optionals=1)


class SubscriptionsStub:
    """Subscriptions unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return subscriptions_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Subscriptions":
        """Create Subscriptions stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SubscriptionsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SubscriptionsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
