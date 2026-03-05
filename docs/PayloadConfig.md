# PayloadConfig

Configuration object that specifies the expected notification payload.

**Source:** `waylay.services.storage.models.payload_config`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_links** | [**List[SIGN]**](SIGN.md) |  | [optional] 
**reference** | [**AnyOf**](AnyOf.md) |  | [optional] 


## Example

```python
from waylay.services.storage.models.payload_config import PayloadConfig

payload_config = PayloadConfig(signed_links=..., reference=...)

# Create from JSON
payload_config = PayloadConfig.from_json('{ "signed_links": ..., "reference": ... }')

# Export to dictionary
payload_config_dict = payload_config.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


