# EVENTTYPE

Supported notification change event types.

**Source:** `waylay.services.storage.models.eventtype`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DELETE** | `'delete'` |
**PUT** | `'put'` |
**GET** | `'get'` |

## Example

```python
from waylay.services.storage.models.eventtype import EVENTTYPE

# Use enum by value
my_eventtype = EVENTTYPE.DELETE
print(my_eventtype)  # Output: 'delete'

# Or by string value
my_eventtype = EVENTTYPE("delete")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


