# HALEntity

Output model representing a collection of HAL links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Links]**](Links.md) |  | [optional] 

## Example

```python
from waylay.services.storage.models.hal_entity import HALEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HALEntity from a JSON string
hal_entity_instance = HALEntity.from_json(json)
# print the JSON string representation of the object
print HALEntity.to_json()

# convert the object into a dict
hal_entity_dict = hal_entity_instance.to_dict()
# create an instance of HALEntity from a dict
hal_entity_form_dict = hal_entity.from_dict(hal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


