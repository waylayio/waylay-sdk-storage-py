# ValidationError


**Source:** `waylay.services.storage.models.validation_error`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 


## Example

```python
from waylay.services.storage.models.validation_error import ValidationError

validation_error = ValidationError(loc=..., msg=..., type=...)

# Create from JSON
validation_error = ValidationError.from_json('{ "loc": ..., "msg": ..., "type": ... }')

# Export to dictionary
validation_error_dict = validation_error.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


