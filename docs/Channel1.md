# Channel1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SystemChannelConfigInputType**](SystemChannelConfigInputType.md) |  | [optional] [default to SystemChannelConfigInputType.SYSTEM]
**description** | **str** |  | [optional] 
**payload** | [**PayloadConfig**](PayloadConfig.md) |  | [optional] 
**authentication** | [**AuthenticationConfig**](AuthenticationConfig.md) |  | [optional] 
**expiry** | [**Expiry**](Expiry.md) |  | [optional] 
**name** | **str** |  | 
**version** | **str** |  | [optional] 
**method** | [**HTTPMETHOD**](HTTPMETHOD.md) |  | [optional] 

## Example

```python
from waylay.services.storage.models.channel1 import Channel1

# TODO update the JSON string below
json = "{}"
# create an instance of Channel1 from a JSON string
channel1_instance = Channel1.from_json(json)
# print the JSON string representation of the object
print Channel1.to_json()

# convert the object into a dict
channel1_dict = channel1_instance.to_dict()
# create an instance of Channel1 from a dict
channel1_form_dict = channel1.from_dict(channel1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


