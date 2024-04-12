# TenantStatusReport

Response model for a tenant status report.

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

# TODO update the JSON string below
json = "{}"
# create an instance of TenantStatusReport from a JSON string
tenant_status_report_instance = TenantStatusReport.from_json(json)
# print the JSON string representation of the object
print TenantStatusReport.to_json()

# convert the object into a dict
tenant_status_report_dict = tenant_status_report_instance.to_dict()
# create an instance of TenantStatusReport from a dict
tenant_status_report_form_dict = tenant_status_report.from_dict(tenant_status_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


