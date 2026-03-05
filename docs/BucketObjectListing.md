# BucketObjectListing

List of storage object representations.

**Source:** `waylay.services.storage.models.bucket_object_listing`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**objects** | [**List[BucketObject]**](BucketObject.md) |  | 


## Example

```python
from waylay.services.storage.models.bucket_object_listing import BucketObjectListing

bucket_object_listing = BucketObjectListing(links=..., objects=...)

# Create from JSON
bucket_object_listing = BucketObjectListing.from_json(
    '{ "_links": ..., "objects": ... }'
)

# Export to dictionary
bucket_object_listing_dict = bucket_object_listing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


