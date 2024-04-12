# BucketObjectListing

List of storage object representations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Links]**](Links.md) |  | [optional] 
**objects** | [**List[BucketObject]**](BucketObject.md) |  | 

## Example

```python
from waylay.services.storage.models.bucket_object_listing import BucketObjectListing

# TODO update the JSON string below
json = "{}"
# create an instance of BucketObjectListing from a JSON string
bucket_object_listing_instance = BucketObjectListing.from_json(json)
# print the JSON string representation of the object
print BucketObjectListing.to_json()

# convert the object into a dict
bucket_object_listing_dict = bucket_object_listing_instance.to_dict()
# create an instance of BucketObjectListing from a dict
bucket_object_listing_form_dict = bucket_object_listing.from_dict(bucket_object_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


