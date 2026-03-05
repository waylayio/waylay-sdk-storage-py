"""Waylay Storage models.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.system_channel_config_output import SystemChannelConfigOutput
from ..models.web_script_channel_config_output import WebScriptChannelConfigOutput

Channel1: TypeAlias = WebScriptChannelConfigOutput | SystemChannelConfigOutput
"""Channel1."""
