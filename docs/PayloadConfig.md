# PayloadConfig

Configuration object that specifies the expected notification payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_links** | [**List[SIGN]**](SIGN.md) |  | [optional] 
**reference** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from waylay.services.storage.models.payload_config import PayloadConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadConfig from a JSON string
payload_config_instance = PayloadConfig.from_json(json)
# print the JSON string representation of the object
print PayloadConfig.to_json()

# convert the object into a dict
payload_config_dict = payload_config_instance.to_dict()
# create an instance of PayloadConfig from a dict
payload_config_form_dict = payload_config.from_dict(payload_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


