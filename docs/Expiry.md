# Expiry

Input model for expiry parameters.

**Source:** `waylay.services.storage.models.expiry`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** |  | [optional] 
**hours** | **int** |  | [optional] 
**days** | **int** |  | [optional] 


## Example

```python
from waylay.services.storage.models.expiry import Expiry

expiry = Expiry(seconds=..., hours=..., days=...)

# Create from JSON
expiry = Expiry.from_json('{ "seconds": ..., "hours": ..., "days": ... }')

# Export to dictionary
expiry_dict = expiry.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


