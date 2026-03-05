# SubscriptionsListing

List of buckets that support subscriptions.

**Source:** `waylay.services.storage.models.subscriptions_listing`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**buckets** | [**List[Bucket]**](Bucket.md) |  | 


## Example

```python
from waylay.services.storage.models.subscriptions_listing import SubscriptionsListing

subscriptions_listing = SubscriptionsListing(links=..., buckets=...)

# Create from JSON
subscriptions_listing = SubscriptionsListing.from_json(
    '{ "_links": ..., "buckets": ... }'
)

# Export to dictionary
subscriptions_listing_dict = subscriptions_listing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


