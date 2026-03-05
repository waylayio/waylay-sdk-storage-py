# BUCKETPOLICYSTATUS

Possible bucket policy status codes.

**Source:** `waylay.services.storage.models.bucketpolicystatus`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UNKNOWN** | `'unknown'` |
**MISSING** | `'missing'` |
**OUT_DATED** | `'out_dated'` |
**UP_TO_DATE** | `'up_to_date'` |

## Example

```python
from waylay.services.storage.models.bucketpolicystatus import BUCKETPOLICYSTATUS

# Use enum by value
my_bucketpolicystatus = BUCKETPOLICYSTATUS.UNKNOWN
print(my_bucketpolicystatus)  # Output: 'unknown'

# Or by string value
my_bucketpolicystatus = BUCKETPOLICYSTATUS("unknown")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


