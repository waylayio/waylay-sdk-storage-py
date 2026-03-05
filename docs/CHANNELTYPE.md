# CHANNELTYPE

Supported notification channel types.

**Source:** `waylay.services.storage.models.channeltype`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**WEBHOOK** | `'webhook'` |
**WEBSCRIPT** | `'webscript'` |
**SYSTEM** | `'system'` |

## Example

```python
from waylay.services.storage.models.channeltype import CHANNELTYPE

# Use enum by value
my_channeltype = CHANNELTYPE.WEBHOOK
print(my_channeltype)  # Output: 'webhook'

# Or by string value
my_channeltype = CHANNELTYPE("webhook")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


