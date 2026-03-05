# S3PolicyStatement

AWS S3 Policy definition statement.

**Source:** `waylay.services.storage.models.s3_policy_statement`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Resource**](Resource.md) |  | [optional] 


## Example

```python
from waylay.services.storage.models.s3_policy_statement import S3PolicyStatement

s3_policy_statement = S3PolicyStatement(resource=...)

# Create from JSON
s3_policy_statement = S3PolicyStatement.from_json('{ "Resource": ... }')

# Export to dictionary
s3_policy_statement_dict = s3_policy_statement.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


