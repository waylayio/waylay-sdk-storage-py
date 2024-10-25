# Store

Representation of a backend store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 
**type** | [**STORETYPE**](STORETYPE.md) |  | 
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from waylay.services.storage.models.store import Store

# TODO update the JSON string below
json = "{}"
# create an instance of Store from a JSON string
store_instance = Store.from_json(json)
# print the JSON string representation of the object
print Store.to_json()

# convert the object into a dict
store_dict = store_instance.to_dict()
# create an instance of Store from a dict
store_form_dict = store.from_dict(store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


