# BucketConfiguration

Representation of a bucket configuration.

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
**public_policy_json** | **object** |  | [optional] 
**public_policy_type** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from waylay.services.storage.models.bucket_configuration import BucketConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of BucketConfiguration from a JSON string
bucket_configuration_instance = BucketConfiguration.from_json(json)
# print the JSON string representation of the object
print BucketConfiguration.to_json()

# convert the object into a dict
bucket_configuration_dict = bucket_configuration_instance.to_dict()
# create an instance of BucketConfiguration from a dict
bucket_configuration_form_dict = bucket_configuration.from_dict(bucket_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


