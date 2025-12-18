# Subscriptions

Listing object for subscriptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**bucket** | [**Bucket**](Bucket.md) |  | 
**subscriptions** | [**List[SubscriptionConfig]**](SubscriptionConfig.md) |  | 
**warnings** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from waylay.services.storage.models.subscriptions import Subscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriptions from a JSON string
subscriptions_instance = Subscriptions.from_json(json)
# print the JSON string representation of the object
print Subscriptions.to_json()

# convert the object into a dict
subscriptions_dict = subscriptions_instance.to_dict()
# create an instance of Subscriptions from a dict
subscriptions_form_dict = subscriptions.from_dict(subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


