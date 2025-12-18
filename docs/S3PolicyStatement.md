# S3PolicyStatement

AWS S3 Policy definition statement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Resource**](Resource.md) |  | [optional] 

## Example

```python
from waylay.services.storage.models.s3_policy_statement import S3PolicyStatement

# TODO update the JSON string below
json = "{}"
# create an instance of S3PolicyStatement from a JSON string
s3_policy_statement_instance = S3PolicyStatement.from_json(json)
# print the JSON string representation of the object
print S3PolicyStatement.to_json()

# convert the object into a dict
s3_policy_statement_dict = s3_policy_statement_instance.to_dict()
# create an instance of S3PolicyStatement from a dict
s3_policy_statement_form_dict = s3_policy_statement.from_dict(s3_policy_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


