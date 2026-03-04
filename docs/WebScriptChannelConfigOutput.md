# WebScriptChannelConfigOutput

Channel configuration for invoking a waylay webscript.

**Source:** `waylay.services.storage.models.web_script_channel_config_output`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WebScriptChannelConfigInputType**](WebScriptChannelConfigInputType.md) |  | [optional] [default to WebScriptChannelConfigInputType.WEBSCRIPT]
**description** | **str** |  | [optional] 
**payload** | [**PayloadConfig**](PayloadConfig.md) |  | [optional] 
**authentication** | [**AuthenticationConfig**](AuthenticationConfig.md) |  | [optional] 
**expiry** | [**Expiry**](Expiry.md) |  | [optional] 
**name** | **str** |  | 
**version** | **str** |  | [optional] 
**method** | [**HTTPMETHOD**](HTTPMETHOD.md) |  | [optional] 


## Example

```python
from waylay.services.storage.models.web_script_channel_config_output import (
    WebScriptChannelConfigOutput,
)

web_script_channel_config_output = WebScriptChannelConfigOutput(
    type=...,
    description=...,
    payload=...,
    authentication=...,
    expiry=...,
    name=...,
    version=...,
    method=...,
)

# Create from JSON
web_script_channel_config_output = WebScriptChannelConfigOutput.from_json(
    '{ "type": ..., "description": ..., "payload": ..., "authentication": ..., "expiry": ..., "name": ..., "version": ..., "method": ... }'
)

# Export to dictionary
web_script_channel_config_output_dict = web_script_channel_config_output.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


