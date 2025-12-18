# HALLink

Represents a HAL link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**method** | **str** |  | [optional] 
**form_data** | **Dict[str, object]** |  | [optional] 
**headers** | **Dict[str, object]** |  | [optional] 

## Example

```python
from waylay.services.storage.models.hal_link import HALLink

# TODO update the JSON string below
json = "{}"
# create an instance of HALLink from a JSON string
hal_link_instance = HALLink.from_json(json)
# print the JSON string representation of the object
print HALLink.to_json()

# convert the object into a dict
hal_link_dict = hal_link_instance.to_dict()
# create an instance of HALLink from a dict
hal_link_form_dict = hal_link.from_dict(hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


