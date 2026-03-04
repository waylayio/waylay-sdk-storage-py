# SubscriptionConfigOutput

Specification of a notification subscription that forwards to a given channel.

**Source:** `waylay.services.storage.models.subscription_config_output`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**channel** | [**Channel1**](Channel1.md) |  | 
**filters** | [**List[EventFilter]**](EventFilter.md) |  | 


## Example

```python
from waylay.services.storage.models.subscription_config_output import (
    SubscriptionConfigOutput,
)

subscription_config_output = SubscriptionConfigOutput(
    links=..., id=..., title=..., description=..., channel=..., filters=...
)

# Create from JSON
subscription_config_output = SubscriptionConfigOutput.from_json(
    '{ "_links": ..., "id": ..., "title": ..., "description": ..., "channel": ..., "filters": ... }'
)

# Export to dictionary
subscription_config_output_dict = subscription_config_output.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


