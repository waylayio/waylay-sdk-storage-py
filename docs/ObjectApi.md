# waylay.services.storage.ObjectApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_or_move**](ObjectApi.md#copy_or_move) | **PUT** /storage/v1/bucket/{bucket_name}/{target_path} | Copy Or Move Object
[**create_folder**](ObjectApi.md#create_folder) | **PUT** /storage/v1/bucket/{bucket_name}/{object_path}/ | Create Folder
[**list**](ObjectApi.md#list) | **GET** /storage/v1/bucket/{bucket_name}/{object_path} | List Objects
[**remove**](ObjectApi.md#remove) | **DELETE** /storage/v1/bucket/{bucket_name}/{object_path} | Remove Object Or Folder

# **copy_or_move**
> copy_or_move(
> bucket_name: str,
> target_path: str,
> query: CopyOrMoveQuery,
> headers
> ) -> HALEntity

Copy Or Move Object

Copy or move object to new location.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-storage-types` is installed
from waylay.services.storage.models.hal_entity import HALEntity
try:
    # Copy Or Move Object
    # calls `PUT /storage/v1/bucket/{bucket_name}/{target_path}`
    api_response = await waylay_client.storage.object.copy_or_move(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        'target_path_example', # target_path | path param "target_path"
        # query parameters:
        query = {
            'move': False
        },
    )
    print("The response of storage.object.copy_or_move:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.object.copy_or_move: %s\n" % e)
```

### Endpoint
```
PUT /storage/v1/bucket/{bucket_name}/{target_path}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**target_path** | **str** | path parameter `"target_path"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['source']** (dict) <br> **query.source** (Query) | **str** | query parameter `"source"` |  | 
**query['move']** (dict) <br> **query.move** (Query) | **bool** | query parameter `"move"` |  | [optional] [default False]
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`HALEntity`** |  | [HALEntity](HALEntity.md)
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

# **create_folder**
> create_folder(
> bucket_name: str,
> object_path: str,
> query: CreateFolderQuery,
> headers
> ) -> BucketObject

Create Folder

Create a (virtual) folder.  * (`all=true`) force creation of a hidden folder,   having a path element that starts with a `.`.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-storage-types` is installed
from waylay.services.storage.models.bucket_object import BucketObject
try:
    # Create Folder
    # calls `PUT /storage/v1/bucket/{bucket_name}/{object_path}/`
    api_response = await waylay_client.storage.object.create_folder(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        'object_path_example', # object_path | path param "object_path"
        # query parameters:
        query = {
            'all': False
        },
    )
    print("The response of storage.object.create_folder:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.object.create_folder: %s\n" % e)
```

### Endpoint
```
PUT /storage/v1/bucket/{bucket_name}/{object_path}/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**object_path** | **str** | path parameter `"object_path"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['all']** (dict) <br> **query.all** (Query) | **bool** | query parameter `"all"` |  | [optional] [default False]
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`BucketObject`** |  | [BucketObject](BucketObject.md)
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
> bucket_name: str,
> object_path: str,
> query: ListQuery,
> headers
> ) -> ResponseListObject

List Objects

List, inspect or sign objects.  * list the objects of a bucket with {object_path} prefix     * (`recursive=true`) list content recursively     * (`all=true`) include hidden objects * (`stat=true`) get the meta of the object at {object_path} * (`sign=[GET,PUT,POST]`) fetch presigned urls to operate on {object_path}     * (`all=true`) allow link creation for hidden objects

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-storage-types` is installed
from waylay.services.storage.models.response_list_object import ResponseListObject
try:
    # List Objects
    # calls `GET /storage/v1/bucket/{bucket_name}/{object_path}`
    api_response = await waylay_client.storage.object.list(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        'object_path_example', # object_path | path param "object_path"
        # query parameters:
        query = {
            'stat': False
            'fetch_content_type': False
            'get_as_attachment': True
            'content_length_min': 0
        },
    )
    print("The response of storage.object.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.object.list: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/bucket/{bucket_name}/{object_path}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**object_path** | **str** | path parameter `"object_path"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['stat']** (dict) <br> **query.stat** (Query) | **bool** | query parameter `"stat"` |  | [optional] [default False]
**query['recursive']** (dict) <br> **query.recursive** (Query) | **bool** | query parameter `"recursive"` |  | [optional] 
**query['all']** (dict) <br> **query.all** (Query) | **bool** | query parameter `"all"` |  | [optional] 
**query['start_after']** (dict) <br> **query.start_after** (Query) | **str** | query parameter `"start_after"` |  | [optional] 
**query['fetch_content_type']** (dict) <br> **query.fetch_content_type** (Query) | **bool** | query parameter `"fetch_content_type"` | If true, fetch content type for each object when not already available from the listing (e.g. on s3 stores). This is less efficient but may be necessary for certain use cases. | [optional] [default False]
**query['get_as_attachment']** (dict) <br> **query.get_as_attachment** (Query) | **bool** | query parameter `"get_as_attachment"` |  | [optional] [default True]
**query['sign']** (dict) <br> **query.sign** (Query) | **str** | query parameter `"sign"` |  | [optional] 
**query['max_keys']** (dict) <br> **query.max_keys** (Query) | **int** | query parameter `"max_keys"` |  | [optional] 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**query['expiry_days']** (dict) <br> **query.expiry_days** (Query) | **int** | query parameter `"expiry_days"` |  | [optional] 
**query['expiry_hours']** (dict) <br> **query.expiry_hours** (Query) | **int** | query parameter `"expiry_hours"` |  | [optional] 
**query['expiry_seconds']** (dict) <br> **query.expiry_seconds** (Query) | **int** | query parameter `"expiry_seconds"` |  | [optional] 
**query['content_length_min']** (dict) <br> **query.content_length_min** (Query) | **int** | query parameter `"content_length_min"` |  | [optional] [default 0]
**query['content_length_max']** (dict) <br> **query.content_length_max** (Query) | **int** | query parameter `"content_length_max"` |  | [optional] 
**query['content_type']** (dict) <br> **query.content_type** (Query) | **str** | query parameter `"content_type"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResponseListObject`** |  | [ResponseListObject](ResponseListObject.md)
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

# **remove**
> remove(
> bucket_name: str,
> object_path: str,
> query: RemoveQuery,
> headers
> ) -> HALEntity

Remove Object Or Folder

Remove the object or folder at {object_path}.  An {object_path} ending in a `/` requests folder deletion of an empty folder unless: * (`recursive=true`) forces recursive deletion of a (non-empty) folder. * (`all=true`) forces recursive deletion, including hidden objects.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-storage-types` is installed
from waylay.services.storage.models.hal_entity import HALEntity
try:
    # Remove Object Or Folder
    # calls `DELETE /storage/v1/bucket/{bucket_name}/{object_path}`
    api_response = await waylay_client.storage.object.remove(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        'object_path_example', # object_path | path param "object_path"
        # query parameters:
        query = {
        },
    )
    print("The response of storage.object.remove:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.object.remove: %s\n" % e)
```

### Endpoint
```
DELETE /storage/v1/bucket/{bucket_name}/{object_path}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**object_path** | **str** | path parameter `"object_path"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['recursive']** (dict) <br> **query.recursive** (Query) | **bool** | query parameter `"recursive"` |  | [optional] 
**query['all']** (dict) <br> **query.all** (Query) | **bool** | query parameter `"all"` |  | [optional] 
**query['start_after']** (dict) <br> **query.start_after** (Query) | **str** | query parameter `"start_after"` |  | [optional] 
**query['max_keys']** (dict) <br> **query.max_keys** (Query) | **int** | query parameter `"max_keys"` |  | [optional] 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`HALEntity`** |  | [HALEntity](HALEntity.md)
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

