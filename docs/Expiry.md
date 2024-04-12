# Expiry

Input model for expiry parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** |  | [optional] 
**hours** | **int** |  | [optional] 
**days** | **int** |  | [optional] 

## Example

```python
from waylay.services.storage.models.expiry import Expiry

# TODO update the JSON string below
json = "{}"
# create an instance of Expiry from a JSON string
expiry_instance = Expiry.from_json(json)
# print the JSON string representation of the object
print Expiry.to_json()

# convert the object into a dict
expiry_dict = expiry_instance.to_dict()
# create an instance of Expiry from a dict
expiry_form_dict = expiry.from_dict(expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


