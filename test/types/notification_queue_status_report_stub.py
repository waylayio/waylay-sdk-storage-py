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
    from waylay.services.storage.models.notification_queue_status_report import (
        NotificationQueueStatusReport,
    )

    NotificationQueueStatusReportAdapter = TypeAdapter(NotificationQueueStatusReport)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

notification_queue_status_report_model_schema = json.loads(
    r"""{
  "required" : [ "notification_queues", "store" ],
  "type" : "object",
  "properties" : {
    "store" : {
      "title" : "Store",
      "type" : "string"
    },
    "notification_queues" : {
      "title" : "Notification Queues",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/NotificationQueueStatus"
      }
    },
    "messages" : {
      "title" : "Messages",
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    }
  },
  "description" : "Response model for a notification queue status report."
}
""",
    object_hook=with_example_provider,
)
notification_queue_status_report_model_schema.update({"definitions": MODEL_DEFINITIONS})

notification_queue_status_report_faker = JSF(
    notification_queue_status_report_model_schema, allow_none_optionals=1
)


class NotificationQueueStatusReportStub:
    """NotificationQueueStatusReport unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return notification_queue_status_report_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "NotificationQueueStatusReport":
        """Create NotificationQueueStatusReport stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                NotificationQueueStatusReportAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return NotificationQueueStatusReportAdapter.validate_python(
            json, context={"skip_validation": True}
        )
