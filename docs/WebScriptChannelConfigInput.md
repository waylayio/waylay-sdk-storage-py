# WebScriptChannelConfigInput

Channel configuration for invoking a waylay webscript.

**Source:** `waylay.services.storage.models.web_script_channel_config_input`




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
from waylay.services.storage.models.web_script_channel_config_input import (
    WebScriptChannelConfigInput,
)

web_script_channel_config_input = WebScriptChannelConfigInput(
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
web_script_channel_config_input = WebScriptChannelConfigInput.from_json(
    '{ "type": ..., "description": ..., "payload": ..., "authentication": ..., "expiry": ..., "name": ..., "version": ..., "method": ... }'
)

# Export to dictionary
web_script_channel_config_input_dict = web_script_channel_config_input.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


