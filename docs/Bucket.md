# Bucket

Representation of a storage bucket.

**Source:** `waylay.services.storage.models.bucket`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**alias** | **str** |  | [optional] 
**name** | **str** |  | 
**store** | [**Store**](Store.md) |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**size** | **int** |  | [optional] 


## Example

```python
from waylay.services.storage.models.bucket import Bucket

bucket = Bucket(links=..., alias=..., name=..., store=..., creation_date=..., size=...)

# Create from JSON
bucket = Bucket.from_json(
    '{ "_links": ..., "alias": ..., "name": ..., "store": ..., "creation_date": ..., "size": ... }'
)

# Export to dictionary
bucket_dict = bucket.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


