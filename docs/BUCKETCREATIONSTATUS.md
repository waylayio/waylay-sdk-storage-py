# BUCKETCREATIONSTATUS

Possbile bucket creation status codes.

**Source:** `waylay.services.storage.models.bucketcreationstatus`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UNKNOWN** | `'unknown'` |
**MISSING** | `'missing'` |
**INVALID** | `'invalid'` |
**UP_TO_DATE** | `'up_to_date'` |

## Example

```python
from waylay.services.storage.models.bucketcreationstatus import BUCKETCREATIONSTATUS

# Use enum by value
my_bucketcreationstatus = BUCKETCREATIONSTATUS.UNKNOWN
print(my_bucketcreationstatus)  # Output: 'unknown'

# Or by string value
my_bucketcreationstatus = BUCKETCREATIONSTATUS("unknown")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


