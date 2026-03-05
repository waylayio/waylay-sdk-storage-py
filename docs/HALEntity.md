# HALEntity

Output model representing a collection of HAL links.

**Source:** `waylay.services.storage.models.hal_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, LinksValue]**](LinksValue.md) |  | [optional] 


## Example

```python
from waylay.services.storage.models.hal_entity import HALEntity

hal_entity = HALEntity(links=...)

# Create from JSON
hal_entity = HALEntity.from_json('{ "_links": ... }')

# Export to dictionary
hal_entity_dict = hal_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


