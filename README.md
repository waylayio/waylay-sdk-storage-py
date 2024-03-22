# Waylay Storage Service

Manage storage buckets and subscriptions.


This Python package is automatically generated based on the 
Waylay Storage OpenAPI specification (API version: v0.4.0)

It consists of two sub-packages that are both plugins for the  package.
- The `waylay-sdk-storage` sub-package contains the Storage api methods.
- The `waylay-sdk-storage-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-storage`.

## Requirements.
This package requires Python 3.11+.

## Installation
Typically this package is installed when installing the [waylay-sdk](https://github.com/waylayio/waylay-sdk-py) package to enable the service's functionality.
When the service api methods are required, waylay-sdk-storage is included in:
- ```pip install waylay-sdk[storage]``` to install `waylay-sdk` along with only this service, or
- ```pip install waylay-sdk[services]``` to install `waylay-sdk` along with all services.
When the typed models are required, both waylay-sdk-storage and waylay-sdk-storage-types are included in:
- ```pip install waylay-sdk[storage,storage-types]``` to install `waylay-sdk` along with only this service including the typed models, or
- ```pip install waylay-sdk[storage]``` to install `waylay-sdk` along with all services along with the typed models.

## Usage


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


## Documentation for API Endpoints

All URIs are relative to *https://api-aws-dev.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AboutApi* | [**status**](docs/AboutApi.md#status) | **GET** /storage/v1/status | Status
*AboutApi* | [**version**](docs/AboutApi.md#version) | **GET** /storage/v1/ | Version
*BucketApi* | [**get**](docs/BucketApi.md#get) | **GET** /storage/v1/bucket/{bucket_name} | Get Bucket
*BucketApi* | [**list**](docs/BucketApi.md#list) | **GET** /storage/v1/bucket | List Buckets
*ObjectApi* | [**copy_or_move**](docs/ObjectApi.md#copy_or_move) | **PUT** /storage/v1/bucket/{bucket_name}/{target_path} | Copy Or Move Object
*ObjectApi* | [**create_folder**](docs/ObjectApi.md#create_folder) | **PUT** /storage/v1/bucket/{bucket_name}/{object_path}/ | Create Folder
*ObjectApi* | [**list**](docs/ObjectApi.md#list) | **GET** /storage/v1/bucket/{bucket_name}/{object_path} | List Objects
*ObjectApi* | [**remove**](docs/ObjectApi.md#remove) | **DELETE** /storage/v1/bucket/{bucket_name}/{object_path} | Remove Object Or Folder
*SubscriptionApi* | [**create**](docs/SubscriptionApi.md#create) | **POST** /storage/v1/subscription/{bucket_name} | Create Bucket Subscription
*SubscriptionApi* | [**delete_by**](docs/SubscriptionApi.md#delete_by) | **DELETE** /storage/v1/subscription/{bucket_name} | Delete All Bucket Subscriptions
*SubscriptionApi* | [**get**](docs/SubscriptionApi.md#get) | **GET** /storage/v1/subscription/{bucket_name}/{subscription_id} | Get Bucket Subscription
*SubscriptionApi* | [**list**](docs/SubscriptionApi.md#list) | **GET** /storage/v1/subscription | Query All Subscriptions
*SubscriptionApi* | [**query**](docs/SubscriptionApi.md#query) | **GET** /storage/v1/subscription/{bucket_name} | Query Bucket Subscriptions
*SubscriptionApi* | [**remove**](docs/SubscriptionApi.md#remove) | **DELETE** /storage/v1/subscription/{bucket_name}/{subscription_id} | Delete Bucket Subscription
*SubscriptionApi* | [**replace**](docs/SubscriptionApi.md#replace) | **PUT** /storage/v1/subscription/{bucket_name}/{subscription_id} | Replace Bucket Subscription


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
 - [EventFilter](docs/EventFilter.md)
 - [Expiry](docs/Expiry.md)
 - [HALEntity](docs/HALEntity.md)
 - [HALLink](docs/HALLink.md)
 - [HTTPMETHOD](docs/HTTPMETHOD.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Links](docs/Links.md)
 - [LocationInner](docs/LocationInner.md)
 - [NotificationQueueStatus](docs/NotificationQueueStatus.md)
 - [NotificationQueueStatusReport](docs/NotificationQueueStatusReport.md)
 - [PayloadConfig](docs/PayloadConfig.md)
 - [QUEUESETUPSTATUS](docs/QUEUESETUPSTATUS.md)
 - [ResponseList](docs/ResponseList.md)
 - [SIGN](docs/SIGN.md)
 - [STORETYPE](docs/STORETYPE.md)
 - [Store](docs/Store.md)
 - [SubscriptionConfig](docs/SubscriptionConfig.md)
 - [Subscriptions](docs/Subscriptions.md)
 - [SubscriptionsListing](docs/SubscriptionsListing.md)
 - [SystemChannelConfig](docs/SystemChannelConfig.md)
 - [TenantStatusReport](docs/TenantStatusReport.md)
 - [VENTTYPE](docs/VENTTYPE.md)
 - [ValidationError](docs/ValidationError.md)
 - [WebScriptChannelConfig](docs/WebScriptChannelConfig.md)

