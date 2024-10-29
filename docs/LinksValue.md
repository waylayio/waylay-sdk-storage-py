# LinksValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**method** | **str** |  | [optional] 
**form_data** | **object** |  | [optional] 
**headers** | **object** |  | [optional] 

## Example

```python
from waylay.services.storage.models.links_value import LinksValue

# TODO update the JSON string below
json = "{}"
# create an instance of LinksValue from a JSON string
links_value_instance = LinksValue.from_json(json)
# print the JSON string representation of the object
print LinksValue.to_json()

# convert the object into a dict
links_value_dict = links_value_instance.to_dict()
# create an instance of LinksValue from a dict
links_value_form_dict = links_value.from_dict(links_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


