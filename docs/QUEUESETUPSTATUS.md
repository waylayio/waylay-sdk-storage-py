# QUEUESETUPSTATUS

Possbile queue setup status codes.

**Source:** `waylay.services.storage.models.queuesetupstatus`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UNKNOWN** | `'unknown'` |
**MISSING** | `'missing'` |
**INVALID** | `'invalid'` |
**NOT_SPECIFIED** | `'not_specified'` |
**UP_TO_DATE** | `'up_to_date'` |

## Example

```python
from waylay.services.storage.models.queuesetupstatus import QUEUESETUPSTATUS

# Use enum by value
my_queuesetupstatus = QUEUESETUPSTATUS.UNKNOWN
print(my_queuesetupstatus)  # Output: 'unknown'

# Or by string value
my_queuesetupstatus = QUEUESETUPSTATUS("unknown")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


