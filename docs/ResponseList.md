# ResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Links]**](Links.md) |  | [optional] 
**objects** | [**List[BucketObject]**](BucketObject.md) |  | 
**bucket** | [**Bucket**](Bucket.md) |  | 
**name** | **str** |  | 
**last_modified** | **datetime** |  | [optional] 
**etag** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**is_dir** | **bool** |  | [optional] [default to False]
**storage_class** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 

## Example

```python
from waylay.services.storage.models.response_list import ResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseList from a JSON string
response_list_instance = ResponseList.from_json(json)
# print the JSON string representation of the object
print ResponseList.to_json()

# convert the object into a dict
response_list_dict = response_list_instance.to_dict()
# create an instance of ResponseList from a dict
response_list_form_dict = response_list.from_dict(response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


