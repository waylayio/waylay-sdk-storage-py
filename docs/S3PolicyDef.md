# S3PolicyDef

AWS S3 Policy definition.

**Source:** `waylay.services.storage.models.s3_policy_def`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | [**List[S3PolicyStatement]**](S3PolicyStatement.md) |  | [optional] 
**version** | **str** |  | [optional] 


## Example

```python
from waylay.services.storage.models.s3_policy_def import S3PolicyDef

s3_policy_def = S3PolicyDef(statement=..., version=...)

# Create from JSON
s3_policy_def = S3PolicyDef.from_json('{ "Statement": ..., "Version": ... }')

# Export to dictionary
s3_policy_def_dict = s3_policy_def.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


