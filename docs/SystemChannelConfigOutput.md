# SystemChannelConfigOutput

Channel configuration for functionality that is fixed by the platform.  This cannot be selected by the end user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SystemChannelConfigInputType**](SystemChannelConfigInputType.md) |  | [optional] [default to SystemChannelConfigInputType.SYSTEM]
**description** | **str** |  | [optional] 
**payload** | [**PayloadConfig**](PayloadConfig.md) |  | [optional] 
**authentication** | [**AuthenticationConfig**](AuthenticationConfig.md) |  | [optional] 
**expiry** | [**Expiry**](Expiry.md) |  | [optional] 

## Example

```python
from waylay.services.storage.models.system_channel_config_output import SystemChannelConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SystemChannelConfigOutput from a JSON string
system_channel_config_output_instance = SystemChannelConfigOutput.from_json(json)
# print the JSON string representation of the object
print SystemChannelConfigOutput.to_json()

# convert the object into a dict
system_channel_config_output_dict = system_channel_config_output_instance.to_dict()
# create an instance of SystemChannelConfigOutput from a dict
system_channel_config_output_form_dict = system_channel_config_output.from_dict(system_channel_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


