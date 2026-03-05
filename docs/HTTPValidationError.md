# HTTPValidationError


**Source:** `waylay.services.storage.models.http_validation_error`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 


## Example

```python
from waylay.services.storage.models.http_validation_error import HTTPValidationError

http_validation_error = HTTPValidationError(detail=...)

# Create from JSON
http_validation_error = HTTPValidationError.from_json('{ "detail": ... }')

# Export to dictionary
http_validation_error_dict = http_validation_error.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


