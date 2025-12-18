# S3PolicyDef

AWS S3 Policy definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | [**List[S3PolicyStatement]**](S3PolicyStatement.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from waylay.services.storage.models.s3_policy_def import S3PolicyDef

# TODO update the JSON string below
json = "{}"
# create an instance of S3PolicyDef from a JSON string
s3_policy_def_instance = S3PolicyDef.from_json(json)
# print the JSON string representation of the object
print S3PolicyDef.to_json()

# convert the object into a dict
s3_policy_def_dict = s3_policy_def_instance.to_dict()
# create an instance of S3PolicyDef from a dict
s3_policy_def_form_dict = s3_policy_def.from_dict(s3_policy_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


