"""Waylay Storage model tests.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.storage.models.eventtype import EVENTTYPE

    EVENTTYPEAdapter = TypeAdapter(EVENTTYPE)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

event_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported notification change event types.",
  "enum" : [ "delete", "put", "get" ]
}
""",
    object_hook=with_example_provider,
)
event_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_type_faker = JSF(event_type_model_schema, allow_none_optionals=1)


class EVENTTYPEStub:
    """EVENTTYPE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_type_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "EVENTTYPE":
        """Create EVENTTYPE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(EVENTTYPEAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EVENTTYPEAdapter.validate_python(json, context={"skip_validation": True})
