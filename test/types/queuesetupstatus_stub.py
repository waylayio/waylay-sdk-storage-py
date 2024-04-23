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
    from waylay.services.storage.models.queuesetupstatus import QUEUESETUPSTATUS

    QUEUESETUPSTATUSAdapter = TypeAdapter(QUEUESETUPSTATUS)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

queue_setup_status_model_schema = json.loads(
    r"""{
  "title" : "QUEUE_SETUP_STATUS",
  "type" : "string",
  "description" : "Possbile queue setup status codes.",
  "enum" : [ "unknown", "missing", "invalid", "not_specified", "up_to_date" ]
}
""",
    object_hook=with_example_provider,
)
queue_setup_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

queue_setup_status_faker = JSF(queue_setup_status_model_schema, allow_none_optionals=1)


class QUEUESETUPSTATUSStub:
    """QUEUESETUPSTATUS unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return queue_setup_status_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "QUEUESETUPSTATUS":
        """Create QUEUESETUPSTATUS stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QUEUESETUPSTATUSAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QUEUESETUPSTATUSAdapter.validate_python(
            json, context={"skip_validation": True}
        )
