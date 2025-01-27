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
    from waylay.services.storage.models.auth import AUTH

    AUTHAdapter = TypeAdapter(AUTH)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

auth_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported authentication methods for notifications.",
  "enum" : [ "DEFAULT", "NONE", "API_KEY", "TOKEN", "WAYLAY_APP", "WAYLAY_TOKEN", "WEBSCRIPT" ]
}
""",
    object_hook=with_example_provider,
)
auth_model_schema.update({"definitions": MODEL_DEFINITIONS})

auth_faker = JSF(auth_model_schema, allow_none_optionals=1)


class AUTHStub:
    """AUTH unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return auth_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AUTH":
        """Create AUTH stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(AUTHAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AUTHAdapter.validate_python(json, context={"skip_validation": True})
