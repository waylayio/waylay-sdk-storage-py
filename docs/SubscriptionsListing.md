# SubscriptionsListing

List of buckets that support subscriptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Links]**](Links.md) |  | [optional] 
**buckets** | [**List[Bucket]**](Bucket.md) |  | 

## Example

```python
from waylay.services.storage.models.subscriptions_listing import SubscriptionsListing

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsListing from a JSON string
subscriptions_listing_instance = SubscriptionsListing.from_json(json)
# print the JSON string representation of the object
print SubscriptionsListing.to_json()

# convert the object into a dict
subscriptions_listing_dict = subscriptions_listing_instance.to_dict()
# create an instance of SubscriptionsListing from a dict
subscriptions_listing_form_dict = subscriptions_listing.from_dict(subscriptions_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


