# SystemChannelConfig

Channel configuration for functionality that is fixed by the platform.  This cannot be selected by the end user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'system']
**description** | **str** |  | [optional] 
**payload** | [**PayloadConfig**](PayloadConfig.md) |  | [optional] 
**authentication** | [**AuthenticationConfig**](AuthenticationConfig.md) |  | [optional] 
**expiry** | [**Expiry**](Expiry.md) |  | [optional] 

## Example

```python
from waylay.services.storage.models.system_channel_config import SystemChannelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SystemChannelConfig from a JSON string
system_channel_config_instance = SystemChannelConfig.from_json(json)
# print the JSON string representation of the object
print SystemChannelConfig.to_json()

# convert the object into a dict
system_channel_config_dict = system_channel_config_instance.to_dict()
# create an instance of SystemChannelConfig from a dict
system_channel_config_form_dict = system_channel_config.from_dict(system_channel_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


