# waylay.services.storage.BucketApi

All URIs are relative to *https://api-aws-dev.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](BucketApi.md#get) | **GET** /storage/v1/bucket/{bucket_name} | Get Bucket
[**list**](BucketApi.md#list) | **GET** /storage/v1/bucket | List Buckets

# **get**
> get(
> bucket_name: str,
> query: GetQuery,
> headers
> ) -> Bucket

Get Bucket

Get a descriptive representation of a bucket.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-storage-types` is installed
from waylay.services.storage.models.bucket import Bucket
try:
    # Get Bucket
    # calls `GET /storage/v1/bucket/{bucket_name}`
    api_response = await waylay_client.storage.bucket.get(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        # query parameters:
        query = {
        },
    )
    print("The response of storage.bucket.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.bucket.get: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/bucket/{bucket_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`Bucket`** |  | [Bucket](Bucket.md)
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

# **list**
> list(
> query: ListQuery,
> headers
> ) -> BucketListing

List Buckets

List authorized buckets.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-storage-types` is installed
from waylay.services.storage.models.bucket_listing import BucketListing
try:
    # List Buckets
    # calls `GET /storage/v1/bucket`
    api_response = await waylay_client.storage.bucket.list(
        # query parameters:
        query = {
        },
    )
    print("The response of storage.bucket.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.bucket.list: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/bucket
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`BucketListing`** |  | [BucketListing](BucketListing.md)
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

