# SubscriptionConfigInput

Specification of a notification subscription that forwards to a given channel.

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
from waylay.services.storage.models.subscription_config_input import SubscriptionConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionConfigInput from a JSON string
subscription_config_input_instance = SubscriptionConfigInput.from_json(json)
# print the JSON string representation of the object
print SubscriptionConfigInput.to_json()

# convert the object into a dict
subscription_config_input_dict = subscription_config_input_instance.to_dict()
# create an instance of SubscriptionConfigInput from a dict
subscription_config_input_form_dict = subscription_config_input.from_dict(subscription_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


