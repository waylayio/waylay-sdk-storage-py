# NotificationQueueStatusReport

Response model for a notification queue status report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | **str** |  | 
**notification_queues** | [**List[NotificationQueueStatus]**](NotificationQueueStatus.md) |  | 
**messages** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from waylay.services.storage.models.notification_queue_status_report import NotificationQueueStatusReport

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationQueueStatusReport from a JSON string
notification_queue_status_report_instance = NotificationQueueStatusReport.from_json(json)
# print the JSON string representation of the object
print NotificationQueueStatusReport.to_json()

# convert the object into a dict
notification_queue_status_report_dict = notification_queue_status_report_instance.to_dict()
# create an instance of NotificationQueueStatusReport from a dict
notification_queue_status_report_form_dict = notification_queue_status_report.from_dict(notification_queue_status_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


