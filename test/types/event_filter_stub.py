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
    from waylay.services.storage.models.event_filter import EventFilter

    EventFilterAdapter = TypeAdapter(EventFilter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

event_filter_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "prefix" : {
      "title" : "Prefix",
      "type" : "string"
    },
    "suffix" : {
      "title" : "Suffix",
      "type" : "string"
    },
    "events" : {
      "uniqueItems" : true,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/VENT_TYPE"
      },
      "default" : [ "put" ]
    },
    "description" : {
      "title" : "Description",
      "type" : "string"
    },
    "queue" : {
      "title" : "Queue",
      "type" : "string"
    }
  },
  "description" : "Filter on change events in a storage backend.\n\nThe `prefix` and `suffix` properties are conditions on the object path\n(not including the bucket name). When not specified, all paths in the bucket will selected.\n\nThe `events` property can contain `put` and/or `delete` values, corresponding\nto create/update and deletion events.\nWhen not specified, only the create/update events are filtered."
}
""",
    object_hook=with_example_provider,
)
event_filter_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_filter_faker = JSF(event_filter_model_schema, allow_none_optionals=1)


class EventFilterStub:
    """EventFilter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_filter_faker.generate()

    @classmethod
    def create_instance(cls) -> "EventFilter":
        """Create EventFilter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return EventFilterAdapter.validate_python(cls.create_json())