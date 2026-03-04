# NotificationQueueStatusReport

Response model for a notification queue status report.

**Source:** `waylay.services.storage.models.notification_queue_status_report`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | **str** |  | 
**notification_queues** | [**List[NotificationQueueStatus]**](NotificationQueueStatus.md) |  | 
**messages** | **List[Dict[str, object]]** |  | [optional] 


## Example

```python
from waylay.services.storage.models.notification_queue_status_report import (
    NotificationQueueStatusReport,
)

notification_queue_status_report = NotificationQueueStatusReport(
    store=..., notification_queues=..., messages=...
)

# Create from JSON
notification_queue_status_report = NotificationQueueStatusReport.from_json(
    '{ "store": ..., "notification_queues": ..., "messages": ... }'
)

# Export to dictionary
notification_queue_status_report_dict = notification_queue_status_report.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


