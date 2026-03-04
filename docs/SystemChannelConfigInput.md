# SystemChannelConfigInput

Channel configuration for functionality that is fixed by the platform.  This cannot be selected by the end user.

**Source:** `waylay.services.storage.models.system_channel_config_input`




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
from waylay.services.storage.models.system_channel_config_input import (
    SystemChannelConfigInput,
)

system_channel_config_input = SystemChannelConfigInput(
    type=..., description=..., payload=..., authentication=..., expiry=...
)

# Create from JSON
system_channel_config_input = SystemChannelConfigInput.from_json(
    '{ "type": ..., "description": ..., "payload": ..., "authentication": ..., "expiry": ... }'
)

# Export to dictionary
system_channel_config_input_dict = system_channel_config_input.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


