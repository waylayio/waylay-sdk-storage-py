# BucketListing

List of Bucket representations.

**Source:** `waylay.services.storage.models.bucket_listing`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**buckets** | [**List[Bucket]**](Bucket.md) |  | 


## Example

```python
from waylay.services.storage.models.bucket_listing import BucketListing

bucket_listing = BucketListing(links=..., buckets=...)

# Create from JSON
bucket_listing = BucketListing.from_json('{ "_links": ..., "buckets": ... }')

# Export to dictionary
bucket_listing_dict = bucket_listing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


