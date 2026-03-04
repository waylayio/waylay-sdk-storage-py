# BucketConfiguration

Representation of a bucket configuration.

**Source:** `waylay.services.storage.models.bucket_configuration`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**alias** | **str** |  | [optional] 
**name** | **str** |  | 
**store** | [**Store**](Store.md) |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | [**BUCKETCREATIONSTATUS**](BUCKETCREATIONSTATUS.md) |  | [optional] 
**public_policy_json** | [**S3PolicyDef**](S3PolicyDef.md) |  | [optional] 
**public_policy_type** | **str** |  | [optional] 
**error** | **str** |  | [optional] 


## Example

```python
from waylay.services.storage.models.bucket_configuration import BucketConfiguration

bucket_configuration = BucketConfiguration(
    links=...,
    alias=...,
    name=...,
    store=...,
    creation_date=...,
    size=...,
    status=...,
    public_policy_json=...,
    public_policy_type=...,
    error=...,
)

# Create from JSON
bucket_configuration = BucketConfiguration.from_json(
    '{ "_links": ..., "alias": ..., "name": ..., "store": ..., "creation_date": ..., "size": ..., "status": ..., "public_policy_json": ..., "public_policy_type": ..., "error": ... }'
)

# Export to dictionary
bucket_configuration_dict = bucket_configuration.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


