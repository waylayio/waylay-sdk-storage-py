# TenantStatusReport

Response model for a tenant status report.

**Source:** `waylay.services.storage.models.tenant_status_report`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | **str** |  | 
**buckets** | [**List[BucketConfiguration]**](BucketConfiguration.md) |  | [optional] 
**queues** | [**List[NotificationQueueStatusReport]**](NotificationQueueStatusReport.md) |  | [optional] 
**total_size** | **int** |  | [optional] 
**bucket_status** | [**BUCKETCREATIONSTATUS**](BUCKETCREATIONSTATUS.md) |  | [optional] 
**policy_status** | [**BUCKETPOLICYSTATUS**](BUCKETPOLICYSTATUS.md) |  | [optional] 
**queue_status** | [**QUEUESETUPSTATUS**](QUEUESETUPSTATUS.md) |  | [optional] 


## Example

```python
from waylay.services.storage.models.tenant_status_report import TenantStatusReport

tenant_status_report = TenantStatusReport(
    tenant=...,
    buckets=...,
    queues=...,
    total_size=...,
    bucket_status=...,
    policy_status=...,
    queue_status=...,
)

# Create from JSON
tenant_status_report = TenantStatusReport.from_json(
    '{ "tenant": ..., "buckets": ..., "queues": ..., "total_size": ..., "bucket_status": ..., "policy_status": ..., "queue_status": ... }'
)

# Export to dictionary
tenant_status_report_dict = tenant_status_report.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


