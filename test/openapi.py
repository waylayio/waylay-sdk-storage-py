import json

import yaml


def with_example_provider(dct):
    has_example = False
    if "example" in dct:
        example, has_example = dct["example"], True
    elif "examples" in dct:
        examples = dct["examples"]
        if isinstance(examples, list) and list:
            example, has_example = examples[0], True
    elif "default" in dct:
        example, has_example = dct["default"], True

    if has_example:
        provider = (
            example
            if example is None or isinstance(example, (dict, list, int, float, bool))
            else f"'{example}'"
        )
        dct.update({"$provider": f"lambda: {provider}"})
    return dct


with open("openapi/storage.transformed.openapi.yaml", "r") as file:
    OPENAPI_SPEC = yaml.safe_load(file)

MODEL_DEFINITIONS = OPENAPI_SPEC["components"]["schemas"]

_auth_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported authentication methods for notifications.",
  "enum" : [ "DEFAULT", "NONE", "API_KEY", "TOKEN", "WAYLAY_APP", "WAYLAY_TOKEN", "WEBSCRIPT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AUTH": _auth_model_schema})

_authentication_config_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "method" : {
      "$ref" : "#/components/schemas/AUTH"
    },
    "key" : {
      "type" : "string",
      "nullable" : true
    },
    "secret" : {
      "type" : "string",
      "nullable" : true
    }
  },
  "description" : "Authentication configuration when forwarding an event to a channel."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AuthenticationConfig": _authentication_config_model_schema})

_bucket_creation_status_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Possbile bucket creation status codes.",
  "enum" : [ "unknown", "missing", "invalid", "up_to_date" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BUCKET_CREATION_STATUS": _bucket_creation_status_model_schema
})

_bucket_policy_status_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Possible bucket policy status codes.",
  "enum" : [ "unknown", "missing", "out_dated", "up_to_date" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BUCKET_POLICY_STATUS": _bucket_policy_status_model_schema})

_bucket_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "alias" : {
      "title" : "Alias",
      "type" : "string"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "store" : {
      "$ref" : "#/components/schemas/Store"
    },
    "creation_date" : {
      "title" : "Creation Date",
      "type" : "string",
      "format" : "date-time"
    },
    "size" : {
      "title" : "Size",
      "type" : "integer"
    }
  },
  "description" : "Representation of a storage bucket."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Bucket": _bucket_model_schema})

_bucket_configuration_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "alias" : {
      "title" : "Alias",
      "type" : "string"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "store" : {
      "$ref" : "#/components/schemas/Store"
    },
    "creation_date" : {
      "title" : "Creation Date",
      "type" : "string",
      "format" : "date-time"
    },
    "size" : {
      "title" : "Size",
      "type" : "integer"
    },
    "status" : {
      "$ref" : "#/components/schemas/BUCKET_CREATION_STATUS"
    },
    "public_policy_json" : {
      "$ref" : "#/components/schemas/S3PolicyDef"
    },
    "public_policy_type" : {
      "title" : "Public Policy Type",
      "type" : "string"
    },
    "error" : {
      "title" : "Error",
      "type" : "string"
    }
  },
  "description" : "Representation of a bucket configuration."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BucketConfiguration": _bucket_configuration_model_schema})

_bucket_listing_model_schema = json.loads(
    r"""{
  "required" : [ "buckets" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "buckets" : {
      "title" : "Buckets",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Bucket"
      }
    }
  },
  "description" : "List of Bucket representations."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BucketListing": _bucket_listing_model_schema})

_bucket_object_model_schema = json.loads(
    r"""{
  "required" : [ "bucket", "name" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "bucket" : {
      "$ref" : "#/components/schemas/Bucket"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "last_modified" : {
      "title" : "Last Modified",
      "type" : "string",
      "format" : "date-time"
    },
    "etag" : {
      "title" : "Etag",
      "type" : "string"
    },
    "size" : {
      "title" : "Size",
      "type" : "integer"
    },
    "content_type" : {
      "title" : "Content Type",
      "type" : "string"
    },
    "is_dir" : {
      "title" : "Is Dir",
      "type" : "boolean",
      "default" : false
    },
    "storage_class" : {
      "title" : "Storage Class",
      "type" : "string"
    },
    "owner_id" : {
      "title" : "Owner Id",
      "type" : "string"
    },
    "owner_name" : {
      "title" : "Owner Name",
      "type" : "string"
    }
  },
  "description" : "Representation of a storage object."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BucketObject": _bucket_object_model_schema})

_bucket_object_listing_model_schema = json.loads(
    r"""{
  "required" : [ "objects" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "objects" : {
      "title" : "Objects",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/BucketObject"
      }
    }
  },
  "description" : "List of storage object representations."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BucketObjectListing": _bucket_object_listing_model_schema})

_channel_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported notification channel types.",
  "enum" : [ "webhook", "webscript", "system" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CHANNEL_TYPE": _channel_type_model_schema})

_channel_model_schema = json.loads(
    r"""{
  "title" : "Channel",
  "discriminator" : {
    "propertyName" : "type",
    "mapping" : {
      "system" : "#/components/schemas/SystemChannelConfig",
      "webscript" : "#/components/schemas/WebScriptChannelConfig"
    }
  },
  "oneOf" : [ {
    "$ref" : "#/components/schemas/WebScriptChannelConfig"
  }, {
    "$ref" : "#/components/schemas/SystemChannelConfig"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Channel": _channel_model_schema})

_event_filter_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "prefix" : {
      "type" : "string",
      "nullable" : true
    },
    "suffix" : {
      "type" : "string",
      "nullable" : true
    },
    "events" : {
      "title" : "Events",
      "uniqueItems" : true,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/VENT_TYPE"
      },
      "default" : [ "put" ]
    },
    "description" : {
      "type" : "string",
      "nullable" : true
    },
    "queue" : {
      "type" : "string",
      "nullable" : true
    }
  },
  "description" : "Filter on change events in a storage backend.\n\nThe `prefix` and `suffix` properties are conditions on the object path\n(not including the bucket name).\nWhen not specified, all paths in the bucket will selected.\n\nThe `events` property can contain `put` and/or `delete` values, corresponding\nto create/update and deletion events.\nWhen not specified, only the create/update events are filtered."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EventFilter": _event_filter_model_schema})

_expiry_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "seconds" : {
      "type" : "integer",
      "nullable" : true
    },
    "hours" : {
      "type" : "integer",
      "nullable" : true
    },
    "days" : {
      "type" : "integer",
      "nullable" : true
    }
  },
  "description" : "Input model for expiry parameters."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Expiry": _expiry_model_schema})

_hal_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    }
  },
  "description" : "Output model representing a collection of HAL links."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALEntity": _hal_entity_model_schema})

_hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "title" : "Href",
      "type" : "string"
    },
    "method" : {
      "type" : "string",
      "nullable" : true
    },
    "form_data" : {
      "type" : "object",
      "additionalProperties" : true,
      "nullable" : true
    },
    "headers" : {
      "type" : "object",
      "additionalProperties" : true,
      "nullable" : true
    }
  },
  "description" : "Represents a HAL link."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLink": _hal_link_model_schema})

_http_method_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported notification methods.",
  "enum" : [ "GET", "PUT", "POST" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HTTP_METHOD": _http_method_model_schema})

_http_validation_error_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "detail" : {
      "title" : "Detail",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ValidationError"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HTTPValidationError": _http_validation_error_model_schema})

_links_value_model_schema = json.loads(
    r"""{
  "title" : "Links_value",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Links_value": _links_value_model_schema})

_location_inner_model_schema = json.loads(
    r"""{
  "title" : "Location_inner",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "type" : "integer"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Location_inner": _location_inner_model_schema})

_notification_queue_status_model_schema = json.loads(
    r"""{
  "required" : [ "method", "name", "status" ],
  "type" : "object",
  "properties" : {
    "status" : {
      "$ref" : "#/components/schemas/QUEUE_SETUP_STATUS"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "method" : {
      "title" : "Method",
      "type" : "string"
    },
    "configured_parameters" : {
      "title" : "Configured Parameters",
      "type" : "object",
      "additionalProperties" : true
    },
    "actual_parameters" : {
      "title" : "Actual Parameters",
      "type" : "object",
      "additionalProperties" : true
    },
    "error" : {
      "title" : "Error",
      "type" : "string"
    }
  },
  "description" : "Response model for the notification queue configuration."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NotificationQueueStatus": _notification_queue_status_model_schema
})

_notification_queue_status_report_model_schema = json.loads(
    r"""{
  "required" : [ "notification_queues", "store" ],
  "type" : "object",
  "properties" : {
    "store" : {
      "title" : "Store",
      "type" : "string"
    },
    "notification_queues" : {
      "title" : "Notification Queues",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/NotificationQueueStatus"
      }
    },
    "messages" : {
      "title" : "Messages",
      "type" : "array",
      "items" : {
        "type" : "object",
        "additionalProperties" : true
      }
    }
  },
  "description" : "Response model for a notification queue status report."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NotificationQueueStatusReport": _notification_queue_status_report_model_schema
})

_payload_config_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "signed_links" : {
      "title" : "Signed Links",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/SIGN"
      }
    },
    "reference" : {
      "title" : "Reference",
      "nullable" : true,
      "anyOf" : [ ]
    }
  },
  "description" : "Configuration object that specifies the expected notification payload."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PayloadConfig": _payload_config_model_schema})

_queue_setup_status_model_schema = json.loads(
    r"""{
  "title" : "QUEUE_SETUP_STATUS",
  "type" : "string",
  "description" : "Possbile queue setup status codes.",
  "enum" : [ "unknown", "missing", "invalid", "not_specified", "up_to_date" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QUEUE_SETUP_STATUS": _queue_setup_status_model_schema})

_resource_model_schema = json.loads(
    r"""{
  "title" : "Resource",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "type" : "array",
    "items" : {
      "type" : "string"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Resource": _resource_model_schema})

_response_list_model_schema = json.loads(
    r"""{
  "title" : "Response List",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/BucketObjectListing"
  }, {
    "$ref" : "#/components/schemas/BucketObject"
  }, {
    "$ref" : "#/components/schemas/HALEntity"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Response_List": _response_list_model_schema})

_s3_policy_def_model_schema = json.loads(
    r"""{
  "title" : "S3PolicyDef",
  "type" : "object",
  "properties" : {
    "Statement" : {
      "title" : "Statement",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/S3PolicyStatement"
      }
    },
    "Version" : {
      "title" : "Version",
      "type" : "string"
    }
  },
  "additionalProperties" : true,
  "description" : "AWS S3 Policy definition."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"S3PolicyDef": _s3_policy_def_model_schema})

_s3_policy_statement_model_schema = json.loads(
    r"""{
  "title" : "S3PolicyStatement",
  "type" : "object",
  "properties" : {
    "Resource" : {
      "$ref" : "#/components/schemas/Resource"
    }
  },
  "additionalProperties" : true,
  "description" : "AWS S3 Policy definition statement."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"S3PolicyStatement": _s3_policy_statement_model_schema})

_sign_model_schema = json.loads(
    r"""{
  "title" : "SIGN",
  "type" : "string",
  "description" : "Supported `sign` url parameter values.",
  "enum" : [ "GET", "PUT", "POST" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SIGN": _sign_model_schema})

_store_type_model_schema = json.loads(
    r"""{
  "title" : "STORE_TYPE",
  "type" : "string",
  "description" : "Supported backend store types.",
  "enum" : [ "gs", "s3", "azure", "zenko" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"STORE_TYPE": _store_type_model_schema})

_store_model_schema = json.loads(
    r"""{
  "title" : "Store",
  "required" : [ "name", "type", "url" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "type" : {
      "$ref" : "#/components/schemas/STORE_TYPE"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "url" : {
      "title" : "Url",
      "type" : "string"
    }
  },
  "description" : "Representation of a backend store."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Store": _store_model_schema})

_subscription_config_model_schema = json.loads(
    r"""{
  "required" : [ "channel", "filters" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "id" : {
      "title" : "Id",
      "type" : "string"
    },
    "title" : {
      "title" : "Title",
      "type" : "string"
    },
    "description" : {
      "title" : "Description",
      "type" : "string"
    },
    "channel" : {
      "$ref" : "#/components/schemas/Channel"
    },
    "filters" : {
      "title" : "Filters",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/EventFilter"
      }
    }
  },
  "description" : "Specification of a notification subscription that forwards to a given channel."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SubscriptionConfig": _subscription_config_model_schema})

_subscriptions_model_schema = json.loads(
    r"""{
  "required" : [ "bucket", "subscriptions" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "bucket" : {
      "$ref" : "#/components/schemas/Bucket"
    },
    "subscriptions" : {
      "title" : "Subscriptions",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/SubscriptionConfig"
      }
    },
    "warnings" : {
      "title" : "Warnings",
      "type" : "array",
      "items" : {
        "type" : "object",
        "additionalProperties" : true
      }
    }
  },
  "description" : "Listing object for subscriptions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Subscriptions": _subscriptions_model_schema})

_subscriptions_listing_model_schema = json.loads(
    r"""{
  "required" : [ "buckets" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      }
    },
    "buckets" : {
      "title" : "Buckets",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Bucket"
      }
    }
  },
  "description" : "List of buckets that support subscriptions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SubscriptionsListing": _subscriptions_listing_model_schema})

_system_channel_config_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/SystemChannelConfig_type"
    },
    "description" : {
      "type" : "string",
      "nullable" : true
    },
    "payload" : {
      "$ref" : "#/components/schemas/PayloadConfig"
    },
    "authentication" : {
      "$ref" : "#/components/schemas/AuthenticationConfig"
    },
    "expiry" : {
      "$ref" : "#/components/schemas/Expiry"
    }
  },
  "description" : "Channel configuration for functionality that is fixed by the platform.\n\nThis cannot be selected by the end user."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SystemChannelConfig": _system_channel_config_model_schema})

_system_channel_config_type_model_schema = json.loads(
    r"""{
  "title" : "SystemChannelConfig_type",
  "type" : "string",
  "default" : "system",
  "enum" : [ "system" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SystemChannelConfig_type": _system_channel_config_type_model_schema
})

_tenant_status_report_model_schema = json.loads(
    r"""{
  "required" : [ "tenant" ],
  "type" : "object",
  "properties" : {
    "tenant" : {
      "title" : "Tenant",
      "type" : "string"
    },
    "buckets" : {
      "title" : "Buckets",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/BucketConfiguration"
      }
    },
    "queues" : {
      "title" : "Queues",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/NotificationQueueStatusReport"
      }
    },
    "total_size" : {
      "title" : "Total Size",
      "type" : "integer"
    },
    "bucket_status" : {
      "$ref" : "#/components/schemas/BUCKET_CREATION_STATUS"
    },
    "policy_status" : {
      "$ref" : "#/components/schemas/BUCKET_POLICY_STATUS"
    },
    "queue_status" : {
      "$ref" : "#/components/schemas/QUEUE_SETUP_STATUS"
    }
  },
  "description" : "Response model for a tenant status report."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TenantStatusReport": _tenant_status_report_model_schema})

_vent_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported notification change event types.",
  "enum" : [ "delete", "put", "get" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VENT_TYPE": _vent_type_model_schema})

_validation_error_model_schema = json.loads(
    r"""{
  "title" : "ValidationError",
  "required" : [ "loc", "msg", "type" ],
  "type" : "object",
  "properties" : {
    "loc" : {
      "title" : "Location",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Location_inner"
      }
    },
    "msg" : {
      "title" : "Message",
      "type" : "string"
    },
    "type" : {
      "title" : "Error Type",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ValidationError": _validation_error_model_schema})

_web_script_channel_config_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/WebScriptChannelConfig_type"
    },
    "description" : {
      "type" : "string",
      "nullable" : true
    },
    "payload" : {
      "$ref" : "#/components/schemas/PayloadConfig"
    },
    "authentication" : {
      "$ref" : "#/components/schemas/AuthenticationConfig"
    },
    "expiry" : {
      "$ref" : "#/components/schemas/Expiry"
    },
    "name" : {
      "title" : "Name",
      "type" : "string"
    },
    "version" : {
      "type" : "string",
      "nullable" : true
    },
    "method" : {
      "$ref" : "#/components/schemas/HTTP_METHOD"
    }
  },
  "description" : "Channel configuration for invoking a waylay webscript."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebScriptChannelConfig": _web_script_channel_config_model_schema
})

_web_script_channel_config_type_model_schema = json.loads(
    r"""{
  "title" : "WebScriptChannelConfig_type",
  "type" : "string",
  "default" : "webscript",
  "enum" : [ "webscript" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebScriptChannelConfig_type": _web_script_channel_config_type_model_schema
})
