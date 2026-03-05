# Subscriptions

Listing object for subscriptions.

**Source:** `waylay.services.storage.models.subscriptions`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**bucket** | [**Bucket**](Bucket.md) |  | 
**subscriptions** | [**List[SubscriptionConfigOutput]**](SubscriptionConfigOutput.md) |  | 
**warnings** | **List[Dict[str, object]]** |  | [optional] 


## Example

```python
from waylay.services.storage.models.subscriptions import Subscriptions

subscriptions = Subscriptions(links=..., bucket=..., subscriptions=..., warnings=...)

# Create from JSON
subscriptions = Subscriptions.from_json(
    '{ "_links": ..., "bucket": ..., "subscriptions": ..., "warnings": ... }'
)

# Export to dictionary
subscriptions_dict = subscriptions.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


