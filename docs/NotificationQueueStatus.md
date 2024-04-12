# NotificationQueueStatus

Response model for the notification queue configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**QUEUESETUPSTATUS**](QUEUESETUPSTATUS.md) |  | 
**name** | **str** |  | 
**method** | **str** |  | 
**configured_parameters** | **object** |  | [optional] 
**actual_parameters** | **object** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from waylay.services.storage.models.notification_queue_status import NotificationQueueStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationQueueStatus from a JSON string
notification_queue_status_instance = NotificationQueueStatus.from_json(json)
# print the JSON string representation of the object
print NotificationQueueStatus.to_json()

# convert the object into a dict
notification_queue_status_dict = notification_queue_status_instance.to_dict()
# create an instance of NotificationQueueStatus from a dict
notification_queue_status_form_dict = notification_queue_status.from_dict(notification_queue_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


