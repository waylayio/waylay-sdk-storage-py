# NotificationQueueStatus

Response model for the notification queue configuration.

**Source:** `waylay.services.storage.models.notification_queue_status`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**QUEUESETUPSTATUS**](QUEUESETUPSTATUS.md) |  | 
**name** | **str** |  | 
**method** | **str** |  | 
**configured_parameters** | **Dict[str, object]** |  | [optional] 
**actual_parameters** | **Dict[str, object]** |  | [optional] 
**error** | **str** |  | [optional] 


## Example

```python
from waylay.services.storage.models.notification_queue_status import (
    NotificationQueueStatus,
)

notification_queue_status = NotificationQueueStatus(
    status=...,
    name=...,
    method=...,
    configured_parameters=...,
    actual_parameters=...,
    error=...,
)

# Create from JSON
notification_queue_status = NotificationQueueStatus.from_json(
    '{ "status": ..., "name": ..., "method": ..., "configured_parameters": ..., "actual_parameters": ..., "error": ... }'
)

# Export to dictionary
notification_queue_status_dict = notification_queue_status.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


