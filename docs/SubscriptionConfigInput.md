# SubscriptionConfigInput

Specification of a notification subscription that forwards to a given channel.

**Source:** `waylay.services.storage.models.subscription_config_input`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**channel** | [**Channel**](Channel.md) |  | 
**filters** | [**List[EventFilter]**](EventFilter.md) |  | 


## Example

```python
from waylay.services.storage.models.subscription_config_input import (
    SubscriptionConfigInput,
)

subscription_config_input = SubscriptionConfigInput(
    links=..., id=..., title=..., description=..., channel=..., filters=...
)

# Create from JSON
subscription_config_input = SubscriptionConfigInput.from_json(
    '{ "_links": ..., "id": ..., "title": ..., "description": ..., "channel": ..., "filters": ... }'
)

# Export to dictionary
subscription_config_input_dict = subscription_config_input.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


