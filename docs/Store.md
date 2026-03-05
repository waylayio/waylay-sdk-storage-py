# Store

Representation of a backend store.

**Source:** `waylay.services.storage.models.store`




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

store = Store(links=..., type=..., name=..., url=...)

# Create from JSON
store = Store.from_json('{ "_links": ..., "type": ..., "name": ..., "url": ... }')

# Export to dictionary
store_dict = store.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


