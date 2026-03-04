"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.bucket_object import BucketObject
from ..models.bucket_object_listing import BucketObjectListing
from ..models.hal_entity import HALEntity

ResponseListObject: TypeAlias = BucketObjectListing | BucketObject | HALEntity
"""ResponseListObject."""
