# STORETYPE

Supported backend store types.

**Source:** `waylay.services.storage.models.storetype`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**GS** | `'gs'` |
**S3** | `'s3'` |
**AZURE** | `'azure'` |
**ZENKO** | `'zenko'` |

## Example

```python
from waylay.services.storage.models.storetype import STORETYPE

# Use enum by value
my_storetype = STORETYPE.GS
print(my_storetype)  # Output: 'gs'

# Or by string value
my_storetype = STORETYPE("gs")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


