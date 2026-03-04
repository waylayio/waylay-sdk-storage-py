# HALLink

Represents a HAL link.

**Source:** `waylay.services.storage.models.hal_link`




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

hal_link = HALLink(href=..., method=..., form_data=..., headers=...)

# Create from JSON
hal_link = HALLink.from_json(
    '{ "href": ..., "method": ..., "form_data": ..., "headers": ... }'
)

# Export to dictionary
hal_link_dict = hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


