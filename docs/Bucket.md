# Bucket

Representation of a storage bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Links]**](Links.md) |  | [optional] 
**alias** | **str** |  | [optional] 
**name** | **str** |  | 
**store** | [**Store**](Store.md) |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from waylay.services.storage.models.bucket import Bucket

# TODO update the JSON string below
json = "{}"
# create an instance of Bucket from a JSON string
bucket_instance = Bucket.from_json(json)
# print the JSON string representation of the object
print Bucket.to_json()

# convert the object into a dict
bucket_dict = bucket_instance.to_dict()
# create an instance of Bucket from a dict
bucket_form_dict = bucket.from_dict(bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


