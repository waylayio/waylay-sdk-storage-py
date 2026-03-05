# Waylay Storage Service

Manage storage buckets and subscriptions.


This Python package is automatically generated based on the 
Waylay Storage OpenAPI specification (API version: 0.9.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/storage.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-storage` sub-package contains the Storage api methods.
- The `waylay-sdk-storage-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-storage`.

## Requirements.
This package requires Python 3.10+.

## Installation

Normally this package is installed together with support for other services using the [waylay-sdk](https://pypi.org/project/waylay-sdk/) umbrella package:
* `pip install waylay-sdk` will install `waylay-sdk-storage` together with the SDK api packages for other services.
* `pip install waylay-sdk[types-storage]` will additionally install the types package `waylay-sdk-storage-types`.
* `pip install waylay-sdk[types]` will install the types packages for this and all other services.

Alternatively, you can install support for this _storage_ service only, installing or extending an existing [waylay-sdk-core](https://pypi.org/project/waylay-sdk-core/):

- `pip install waylay-sdk-storage` to only install api support for _storage_.
- `pip install waylay-sdk-storage[types]` to additionally install type support for _storage_.

## Usage

```python
# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-storage-types` is installed
from waylay.services.storage.models.tenant_status_report import TenantStatusReport

try:
    # Status
    # calls `GET /storage/v1/status`
    api_response = await waylay_client.storage.about.status(
        # query parameters:
        query={
            "include_buckets": True,
            "include_queues": True,
            "include_disk_usage": False,
        },
    )
    print(f"Response: {api_response}")
except ApiError as e:
    print("Exception when calling storage.about.status: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/sdk/waylay-sdk/).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

SDK Path | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
**waylay_client.storage.about** | [**get**](docs/AboutApi.md#get) | **GET** /storage/v1/ | Version
**waylay_client.storage.about** | [**status**](docs/AboutApi.md#status) | **GET** /storage/v1/status | Status
 | | |
**waylay_client.storage.bucket** | [**get**](docs/BucketApi.md#get) | **GET** /storage/v1/bucket/{bucket_name} | Get Bucket
**waylay_client.storage.bucket** | [**list**](docs/BucketApi.md#list) | **GET** /storage/v1/bucket | List Buckets
 | | |
**waylay_client.storage.object** | [**copy_or_move**](docs/ObjectApi.md#copy_or_move) | **PUT** /storage/v1/bucket/{bucket_name}/{target_path} | Copy Or Move Object
**waylay_client.storage.object** | [**create_folder**](docs/ObjectApi.md#create_folder) | **PUT** /storage/v1/bucket/{bucket_name}/{object_path}/ | Create Folder
**waylay_client.storage.object** | [**list**](docs/ObjectApi.md#list) | **GET** /storage/v1/bucket/{bucket_name}/{object_path} | List Objects
**waylay_client.storage.object** | [**remove**](docs/ObjectApi.md#remove) | **DELETE** /storage/v1/bucket/{bucket_name}/{object_path} | Remove Object Or Folder
 | | |
**waylay_client.storage.subscription** | [**create**](docs/SubscriptionApi.md#create) | **POST** /storage/v1/subscription/{bucket_name} | Create Bucket Subscription
**waylay_client.storage.subscription** | [**delete_by**](docs/SubscriptionApi.md#delete_by) | **DELETE** /storage/v1/subscription/{bucket_name} | Delete All Bucket Subscriptions
**waylay_client.storage.subscription** | [**get**](docs/SubscriptionApi.md#get) | **GET** /storage/v1/subscription/{bucket_name}/{subscription_id} | Get Bucket Subscription
**waylay_client.storage.subscription** | [**list**](docs/SubscriptionApi.md#list) | **GET** /storage/v1/subscription | Query All Subscriptions
**waylay_client.storage.subscription** | [**query**](docs/SubscriptionApi.md#query) | **GET** /storage/v1/subscription/{bucket_name} | Query Bucket Subscriptions
**waylay_client.storage.subscription** | [**remove**](docs/SubscriptionApi.md#remove) | **DELETE** /storage/v1/subscription/{bucket_name}/{subscription_id} | Delete Bucket Subscription
**waylay_client.storage.subscription** | [**replace**](docs/SubscriptionApi.md#replace) | **PUT** /storage/v1/subscription/{bucket_name}/{subscription_id} | Replace Bucket Subscription


## Documentation For Models

 - [AUTH](docs/AUTH.md)
 - [AuthenticationConfig](docs/AuthenticationConfig.md)
 - [BUCKETCREATIONSTATUS](docs/BUCKETCREATIONSTATUS.md)
 - [BUCKETPOLICYSTATUS](docs/BUCKETPOLICYSTATUS.md)
 - [Bucket](docs/Bucket.md)
 - [BucketConfiguration](docs/BucketConfiguration.md)
 - [BucketListing](docs/BucketListing.md)
 - [BucketObject](docs/BucketObject.md)
 - [BucketObjectListing](docs/BucketObjectListing.md)
 - [CHANNELTYPE](docs/CHANNELTYPE.md)
 - [Channel](docs/Channel.md)
 - [Channel1](docs/Channel1.md)
 - [EVENTTYPE](docs/EVENTTYPE.md)
 - [EventFilter](docs/EventFilter.md)
 - [Expiry](docs/Expiry.md)
 - [HALEntity](docs/HALEntity.md)
 - [HALLink](docs/HALLink.md)
 - [HTTPMETHOD](docs/HTTPMETHOD.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LinksValue](docs/LinksValue.md)
 - [LocationInner](docs/LocationInner.md)
 - [NotificationQueueStatus](docs/NotificationQueueStatus.md)
 - [NotificationQueueStatusReport](docs/NotificationQueueStatusReport.md)
 - [PayloadConfig](docs/PayloadConfig.md)
 - [QUEUESETUPSTATUS](docs/QUEUESETUPSTATUS.md)
 - [Resource](docs/Resource.md)
 - [ResponseListObject](docs/ResponseListObject.md)
 - [S3PolicyDef](docs/S3PolicyDef.md)
 - [S3PolicyStatement](docs/S3PolicyStatement.md)
 - [SIGN](docs/SIGN.md)
 - [STORETYPE](docs/STORETYPE.md)
 - [Store](docs/Store.md)
 - [SubscriptionConfigInput](docs/SubscriptionConfigInput.md)
 - [SubscriptionConfigOutput](docs/SubscriptionConfigOutput.md)
 - [Subscriptions](docs/Subscriptions.md)
 - [SubscriptionsListing](docs/SubscriptionsListing.md)
 - [SystemChannelConfigInput](docs/SystemChannelConfigInput.md)
 - [SystemChannelConfigInputType](docs/SystemChannelConfigInputType.md)
 - [SystemChannelConfigOutput](docs/SystemChannelConfigOutput.md)
 - [TenantStatusReport](docs/TenantStatusReport.md)
 - [ValidationError](docs/ValidationError.md)
 - [WebScriptChannelConfigInput](docs/WebScriptChannelConfigInput.md)
 - [WebScriptChannelConfigInputType](docs/WebScriptChannelConfigInputType.md)
 - [WebScriptChannelConfigOutput](docs/WebScriptChannelConfigOutput.md)

