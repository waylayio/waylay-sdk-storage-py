# BucketListing

List of Bucket representations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Links]**](Links.md) |  | [optional] 
**buckets** | [**List[Bucket]**](Bucket.md) |  | 

## Example

```python
from waylay.services.storage.models.bucket_listing import BucketListing

# TODO update the JSON string below
json = "{}"
# create an instance of BucketListing from a JSON string
bucket_listing_instance = BucketListing.from_json(json)
# print the JSON string representation of the object
print BucketListing.to_json()

# convert the object into a dict
bucket_listing_dict = bucket_listing_instance.to_dict()
# create an instance of BucketListing from a dict
bucket_listing_form_dict = bucket_listing.from_dict(bucket_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


