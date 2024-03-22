# coding: utf-8
"""Waylay Storage model tests.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.storage.models.httpmethod import HTTPMETHOD

    HTTPMETHODAdapter = TypeAdapter(HTTPMETHOD)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

http_method_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported notification methods.",
  "enum" : [ "GET", "PUT", "POST" ]
}
""",
    object_hook=with_example_provider,
)
http_method_model_schema.update({"definitions": MODEL_DEFINITIONS})

http_method_faker = JSF(http_method_model_schema, allow_none_optionals=1)


class HTTPMETHODStub:
    """HTTPMETHOD unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return http_method_faker.generate()

    @classmethod
    def create_instance(cls) -> "HTTPMETHOD":
        """Create HTTPMETHOD stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return HTTPMETHODAdapter.validate_python(cls.create_json())
