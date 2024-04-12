# AuthenticationConfig

Configuration for the authentication method used when forwarding an event to a channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**AUTH**](AUTH.md) |  | [optional] 
**key** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from waylay.services.storage.models.authentication_config import AuthenticationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationConfig from a JSON string
authentication_config_instance = AuthenticationConfig.from_json(json)
# print the JSON string representation of the object
print AuthenticationConfig.to_json()

# convert the object into a dict
authentication_config_dict = authentication_config_instance.to_dict()
# create an instance of AuthenticationConfig from a dict
authentication_config_form_dict = authentication_config.from_dict(authentication_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


