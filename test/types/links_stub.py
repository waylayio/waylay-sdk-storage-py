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
    from waylay.services.storage.models.links import Links

    LinksAdapter = TypeAdapter(Links)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

links_model_schema = json.loads(
    r"""{
  "title" : "_Links",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
links_model_schema.update({"definitions": MODEL_DEFINITIONS})

links_faker = JSF(links_model_schema, allow_none_optionals=1)


class LinksStub:
    """Links unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return links_faker.generate()

    @classmethod
    def create_instance(cls) -> "Links":
        """Create Links stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LinksAdapter.validate_python(cls.create_json())
