# WebScriptChannelConfigOutput

Channel configuration for invoking a waylay webscript.

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
from waylay.services.storage.models.web_script_channel_config_output import WebScriptChannelConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WebScriptChannelConfigOutput from a JSON string
web_script_channel_config_output_instance = WebScriptChannelConfigOutput.from_json(json)
# print the JSON string representation of the object
print WebScriptChannelConfigOutput.to_json()

# convert the object into a dict
web_script_channel_config_output_dict = web_script_channel_config_output_instance.to_dict()
# create an instance of WebScriptChannelConfigOutput from a dict
web_script_channel_config_output_form_dict = web_script_channel_config_output.from_dict(web_script_channel_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


