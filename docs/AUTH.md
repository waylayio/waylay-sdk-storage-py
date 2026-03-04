# AUTH

Supported authentication methods for notifications.

**Source:** `waylay.services.storage.models.auth`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DEFAULT** | `'DEFAULT'` |
**NONE** | `'NONE'` |
**API_KEY** | `'API_KEY'` |
**TOKEN** | `'TOKEN'` |
**WAYLAY_APP** | `'WAYLAY_APP'` |
**WAYLAY_TOKEN** | `'WAYLAY_TOKEN'` |
**WEBSCRIPT** | `'WEBSCRIPT'` |

## Example

```python
from waylay.services.storage.models.auth import AUTH

# Use enum by value
my_auth = AUTH.DEFAULT
print(my_auth)  # Output: 'DEFAULT'

# Or by string value
my_auth = AUTH("DEFAULT")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


