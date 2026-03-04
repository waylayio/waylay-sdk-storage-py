# AuthenticationConfig

Authentication configuration when forwarding an event to a channel.

**Source:** `waylay.services.storage.models.authentication_config`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**AUTH**](AUTH.md) |  | [optional] 
**key** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 


## Example

```python
from waylay.services.storage.models.authentication_config import AuthenticationConfig

authentication_config = AuthenticationConfig(method=..., key=..., secret=...)

# Create from JSON
authentication_config = AuthenticationConfig.from_json(
    '{ "method": ..., "key": ..., "secret": ... }'
)

# Export to dictionary
authentication_config_dict = authentication_config.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


