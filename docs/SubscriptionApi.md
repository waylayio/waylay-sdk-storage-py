# waylay.services.storage.SubscriptionApi

All URIs are relative to *https://api-aws-dev.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SubscriptionApi.md#create) | **POST** /storage/v1/subscription/{bucket_name} | Create Bucket Subscription
[**delete_by**](SubscriptionApi.md#delete_by) | **DELETE** /storage/v1/subscription/{bucket_name} | Delete All Bucket Subscriptions
[**get**](SubscriptionApi.md#get) | **GET** /storage/v1/subscription/{bucket_name}/{subscription_id} | Get Bucket Subscription
[**list**](SubscriptionApi.md#list) | **GET** /storage/v1/subscription | Query All Subscriptions
[**query**](SubscriptionApi.md#query) | **GET** /storage/v1/subscription/{bucket_name} | Query Bucket Subscriptions
[**remove**](SubscriptionApi.md#remove) | **DELETE** /storage/v1/subscription/{bucket_name}/{subscription_id} | Delete Bucket Subscription
[**replace**](SubscriptionApi.md#replace) | **PUT** /storage/v1/subscription/{bucket_name}/{subscription_id} | Replace Bucket Subscription

# **create**
> create(
> bucket_name: str,
> query: CreateQuery,
> headers
> ) -> SubscriptionConfig

Create Bucket Subscription

Create a new notification subscription on a bucket with a given or generated id.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.subscription_config import SubscriptionConfig
try:
    # Create Bucket Subscription
    # calls `POST /storage/v1/subscription/{bucket_name}`
    api_response = await waylay_client.storage.subscription.create(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        # query parameters:
        query = {
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.storage.SubscriptionConfig() # SubscriptionConfig | 
    )
    print("The response of storage.subscription.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.subscription.create: %s\n" % e)
```

### Endpoint
```
POST /storage/v1/subscription/{bucket_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**json** | [**SubscriptionConfig**](SubscriptionConfig.md) | json request body |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`SubscriptionConfig`** |  | [SubscriptionConfig](SubscriptionConfig.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_by**
> delete_by(
> bucket_name: str,
> query: DeleteByQuery,
> headers
> ) -> HALEntity

Delete All Bucket Subscriptions

Remove all notification subscription on a bucket that match a given event and/or channel filter.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.channeltype import CHANNELTYPE
from waylay.services.storage.models.hal_entity import HALEntity
from waylay.services.storage.models.venttype import VENTTYPE
try:
    # Delete All Bucket Subscriptions
    # calls `DELETE /storage/v1/subscription/{bucket_name}`
    api_response = await waylay_client.storage.subscription.delete_by(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        # query parameters:
        query = {
            'event_type': 'delete'
            'channel_type': 'webhook'
        },
    )
    print("The response of storage.subscription.delete_by:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.subscription.delete_by: %s\n" % e)
```

### Endpoint
```
DELETE /storage/v1/subscription/{bucket_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['start_after']** (dict) <br> **query.start_after** (Query) | **str** | query parameter `"start_after"` |  | [optional] 
**query['prefix']** (dict) <br> **query.prefix** (Query) | **str** | query parameter `"prefix"` |  | [optional] 
**query['suffix']** (dict) <br> **query.suffix** (Query) | **str** | query parameter `"suffix"` |  | [optional] 
**query['event_type']** (dict) <br> **query.event_type** (Query) | [**VENTTYPE**](.md) | query parameter `"event_type"` |  | [optional] 
**query['channel_type']** (dict) <br> **query.channel_type** (Query) | [**CHANNELTYPE**](.md) | query parameter `"channel_type"` |  | [optional] 
**query['channel_id']** (dict) <br> **query.channel_id** (Query) | **str** | query parameter `"channel_id"` |  | [optional] 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**query['max_keys']** (dict) <br> **query.max_keys** (Query) | **int** | query parameter `"max_keys"` |  | [optional] 
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

# **get**
> get(
> bucket_name: str,
> subscription_id: str,
> query: GetQuery,
> headers
> ) -> SubscriptionConfig

Get Bucket Subscription

Fetch a notification subscription.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.subscription_config import SubscriptionConfig
try:
    # Get Bucket Subscription
    # calls `GET /storage/v1/subscription/{bucket_name}/{subscription_id}`
    api_response = await waylay_client.storage.subscription.get(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        'subscription_id_example', # subscription_id | path param "subscription_id"
        # query parameters:
        query = {
        },
    )
    print("The response of storage.subscription.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.subscription.get: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/subscription/{bucket_name}/{subscription_id}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**subscription_id** | **str** | path parameter `"subscription_id"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`SubscriptionConfig`** |  | [SubscriptionConfig](SubscriptionConfig.md)
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
> ) -> SubscriptionsListing

Query All Subscriptions

List notification subscriptions per bucket that have notification enabled.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.channeltype import CHANNELTYPE
from waylay.services.storage.models.subscriptions_listing import SubscriptionsListing
from waylay.services.storage.models.venttype import VENTTYPE
try:
    # Query All Subscriptions
    # calls `GET /storage/v1/subscription`
    api_response = await waylay_client.storage.subscription.list(
        # query parameters:
        query = {
            'event_type': 'delete'
            'channel_type': 'webhook'
        },
    )
    print("The response of storage.subscription.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.subscription.list: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/subscription
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**query['prefix']** (dict) <br> **query.prefix** (Query) | **str** | query parameter `"prefix"` |  | [optional] 
**query['suffix']** (dict) <br> **query.suffix** (Query) | **str** | query parameter `"suffix"` |  | [optional] 
**query['event_type']** (dict) <br> **query.event_type** (Query) | [**VENTTYPE**](.md) | query parameter `"event_type"` |  | [optional] 
**query['channel_type']** (dict) <br> **query.channel_type** (Query) | [**CHANNELTYPE**](.md) | query parameter `"channel_type"` |  | [optional] 
**query['channel_id']** (dict) <br> **query.channel_id** (Query) | **str** | query parameter `"channel_id"` |  | [optional] 
**query['max_keys']** (dict) <br> **query.max_keys** (Query) | **int** | query parameter `"max_keys"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`SubscriptionsListing`** |  | [SubscriptionsListing](SubscriptionsListing.md)
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

# **query**
> query(
> bucket_name: str,
> query: QueryQuery,
> headers
> ) -> Subscriptions

Query Bucket Subscriptions

List notification subscriptions for given bucket.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.channeltype import CHANNELTYPE
from waylay.services.storage.models.subscriptions import Subscriptions
from waylay.services.storage.models.venttype import VENTTYPE
try:
    # Query Bucket Subscriptions
    # calls `GET /storage/v1/subscription/{bucket_name}`
    api_response = await waylay_client.storage.subscription.query(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        # query parameters:
        query = {
            'event_type': 'delete'
            'channel_type': 'webhook'
        },
    )
    print("The response of storage.subscription.query:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.subscription.query: %s\n" % e)
```

### Endpoint
```
GET /storage/v1/subscription/{bucket_name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['start_after']** (dict) <br> **query.start_after** (Query) | **str** | query parameter `"start_after"` |  | [optional] 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**query['prefix']** (dict) <br> **query.prefix** (Query) | **str** | query parameter `"prefix"` |  | [optional] 
**query['suffix']** (dict) <br> **query.suffix** (Query) | **str** | query parameter `"suffix"` |  | [optional] 
**query['event_type']** (dict) <br> **query.event_type** (Query) | [**VENTTYPE**](.md) | query parameter `"event_type"` |  | [optional] 
**query['channel_type']** (dict) <br> **query.channel_type** (Query) | [**CHANNELTYPE**](.md) | query parameter `"channel_type"` |  | [optional] 
**query['channel_id']** (dict) <br> **query.channel_id** (Query) | **str** | query parameter `"channel_id"` |  | [optional] 
**query['max_keys']** (dict) <br> **query.max_keys** (Query) | **int** | query parameter `"max_keys"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`Subscriptions`** |  | [Subscriptions](Subscriptions.md)
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
> subscription_id: str,
> query: RemoveQuery,
> headers
> ) -> HALEntity

Delete Bucket Subscription

Remove a notification subscription.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.hal_entity import HALEntity
try:
    # Delete Bucket Subscription
    # calls `DELETE /storage/v1/subscription/{bucket_name}/{subscription_id}`
    api_response = await waylay_client.storage.subscription.remove(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        'subscription_id_example', # subscription_id | path param "subscription_id"
        # query parameters:
        query = {
        },
    )
    print("The response of storage.subscription.remove:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.subscription.remove: %s\n" % e)
```

### Endpoint
```
DELETE /storage/v1/subscription/{bucket_name}/{subscription_id}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**subscription_id** | **str** | path parameter `"subscription_id"` |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
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

# **replace**
> replace(
> bucket_name: str,
> subscription_id: str,
> query: ReplaceQuery,
> headers
> ) -> SubscriptionConfig

Replace Bucket Subscription

Create or replace a notification subscription on a bucket with a given id.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.storage.models.subscription_config import SubscriptionConfig
try:
    # Replace Bucket Subscription
    # calls `PUT /storage/v1/subscription/{bucket_name}/{subscription_id}`
    api_response = await waylay_client.storage.subscription.replace(
        'bucket_name_example', # bucket_name | path param "bucket_name"
        'subscription_id_example', # subscription_id | path param "subscription_id"
        # query parameters:
        query = {
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.storage.SubscriptionConfig() # SubscriptionConfig | 
    )
    print("The response of storage.subscription.replace:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling storage.subscription.replace: %s\n" % e)
```

### Endpoint
```
PUT /storage/v1/subscription/{bucket_name}/{subscription_id}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**bucket_name** | **str** | path parameter `"bucket_name"` |  | 
**subscription_id** | **str** | path parameter `"subscription_id"` |  | 
**json** | [**SubscriptionConfig**](SubscriptionConfig.md) | json request body |  | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['store']** (dict) <br> **query.store** (Query) | **str** | query parameter `"store"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`SubscriptionConfig`** |  | [SubscriptionConfig](SubscriptionConfig.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

