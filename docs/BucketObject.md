# BucketObject

Representation of a storage object.

**Source:** `waylay.services.storage.models.bucket_object`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
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
from waylay.services.storage.models.bucket_object import BucketObject

bucket_object = BucketObject(
    links=...,
    bucket=...,
    name=...,
    last_modified=...,
    etag=...,
    size=...,
    content_type=...,
    is_dir=...,
    storage_class=...,
    owner_id=...,
    owner_name=...,
)

# Create from JSON
bucket_object = BucketObject.from_json(
    '{ "_links": ..., "bucket": ..., "name": ..., "last_modified": ..., "etag": ..., "size": ..., "content_type": ..., "is_dir": ..., "storage_class": ..., "owner_id": ..., "owner_name": ... }'
)

# Export to dictionary
bucket_object_dict = bucket_object.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


