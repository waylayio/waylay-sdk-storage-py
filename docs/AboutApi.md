# waylay.services.storage.AboutApi

All URIs are relative to *https://api-aws-dev.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status**](AboutApi.md#status) | **GET** /storage/v1/status | Status
[**version**](AboutApi.md#version) | **GET** /storage/v1/ | Version

# **status**
> status(
> query: StatusQuery,
> headers
> ) -> TenantStatusReport

Status

Validate consistency of buckets and notification queues for this tenant.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.tenant_status_report import TenantStatusReport
try:
    # Status
    # calls `GET /storage/v1/status`
    api_response = await waylay_client.storage.about.status(
        # query parameters:
        query = {
            'include_buckets': True
            'include_queues': True
            'include_disk_usage': False
        },
    )
    print("The response of storage.about.status:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.about.status: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/status
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**query['include_buckets']** (dict) <br> **query.include_buckets** (Query) | **bool** | query parameter `"include_buckets"` |  | [optional] [default True]
**query['include_queues']** (dict) <br> **query.include_queues** (Query) | **bool** | query parameter `"include_queues"` |  | [optional] [default True]
**query['include_disk_usage']** (dict) <br> **query.include_disk_usage** (Query) | **bool** | query parameter `"include_disk_usage"` |  | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TenantStatusReport`** |  | [TenantStatusReport](TenantStatusReport.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version**
> version(
> headers
> ) -> str

Version

Get the application version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

try:
    # Version
    # calls `GET /storage/v1/`
    api_response = await waylay_client.storage.about.version(
    )
    print("The response of storage.about.version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.about.version: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/
```
### Parameters

This endpoint does not need any parameter.
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`str`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

