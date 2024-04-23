# coding: utf-8
"""Waylay Storage api.

This code was generated from the OpenAPI documentation of 'Waylay Storage'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Literal,
    TypeVar,
    overload,
)

from pydantic import (
    StrictBool,
    StrictStr,
    TypeAdapter,
)
from waylay.sdk.api import (
    HeaderTypes,
    QueryParamTypes,
    Response,
)
from waylay.sdk.api._models import Model
from waylay.sdk.plugin import WithApiClient

if TYPE_CHECKING:
    from waylay.services.storage.models import (
        BucketObject,
        HALEntity,
        HTTPValidationError,
        ResponseList,
    )
    from waylay.services.storage.queries.object_api import (
        CopyOrMoveQuery,
        CreateFolderQuery,
        ListQuery,
        RemoveQuery,
    )


try:
    from waylay.services.storage.models import (
        BucketObject,
        HALEntity,
        HTTPValidationError,
        ResponseList,
    )
    from waylay.services.storage.queries.object_api import (
        CopyOrMoveQuery,
        CreateFolderQuery,
        ListQuery,
        RemoveQuery,
    )

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        CopyOrMoveQuery = dict
        HALEntity = Model

        HTTPValidationError = Model

        CreateFolderQuery = dict
        BucketObject = Model

        HTTPValidationError = Model

        ListQuery = dict
        ResponseList = Model

        HTTPValidationError = Model

        RemoveQuery = dict
        HALEntity = Model

        HTTPValidationError = Model


T = TypeVar("T")


class ObjectApi(WithApiClient):
    """ObjectApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def copy_or_move(
        self,
        bucket_name: StrictStr,
        target_path: StrictStr,
        *,
        query: CopyOrMoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> HALEntity: ...

    @overload
    async def copy_or_move(
        self,
        bucket_name: StrictStr,
        target_path: StrictStr,
        *,
        query: CopyOrMoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def copy_or_move(
        self,
        bucket_name: StrictStr,
        target_path: StrictStr,
        *,
        query: CopyOrMoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def copy_or_move(
        self,
        bucket_name: StrictStr,
        target_path: StrictStr,
        *,
        query: CopyOrMoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def copy_or_move(
        self,
        bucket_name: StrictStr,
        target_path: StrictStr,
        *,
        query: CopyOrMoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def copy_or_move(
        self,
        bucket_name: StrictStr,
        target_path: StrictStr,
        *,
        query: CopyOrMoveQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> HALEntity | T | Response | Model:
        """Copy Or Move Object.

        Copy or move object to new location.
        :param bucket_name: (required)
        :type bucket_name: str
        :param target_path: (required)
        :type target_path: str
        :param query: URL Query parameters.
        :type query: CopyOrMoveQuery | QueryParamTypes, optional
        :param query['source'] (dict) <br> query.source (Query) : (required)
        :type query['source']: str
        :param query['move'] (dict) <br> query.move (Query) :
        :type query['move']: bool
        :param query['store'] (dict) <br> query.store (Query) :
        :type query['store']: str
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "bucket_name": str(bucket_name),
            "target_path": str(target_path),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(CopyOrMoveQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": HALEntity if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "422": HTTPValidationError,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="PUT",
            resource_path="/storage/v1/bucket/{bucket_name}/{target_path}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def create_folder(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: CreateFolderQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> BucketObject: ...

    @overload
    async def create_folder(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: CreateFolderQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def create_folder(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: CreateFolderQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def create_folder(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: CreateFolderQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def create_folder(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: CreateFolderQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def create_folder(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: CreateFolderQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> BucketObject | T | Response | Model:
        """Create Folder.

        Create a (virtual) folder.  * (`all=true`) force creation of a hidden folder,   having a path element that starts with a `.`.
        :param bucket_name: (required)
        :type bucket_name: str
        :param object_path: (required)
        :type object_path: str
        :param query: URL Query parameters.
        :type query: CreateFolderQuery | QueryParamTypes, optional
        :param query['all'] (dict) <br> query.all (Query) :
        :type query['all']: bool
        :param query['store'] (dict) <br> query.store (Query) :
        :type query['store']: str
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "bucket_name": str(bucket_name),
            "object_path": str(object_path),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(CreateFolderQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": BucketObject if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "422": HTTPValidationError,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="PUT",
            resource_path="/storage/v1/bucket/{bucket_name}/{object_path}/",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def list(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResponseList: ...

    @overload
    async def list(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def list(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def list(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def list(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def list(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ResponseList | T | Response | Model:
        """List Objects.

        List, inspect or sign objects.  * list the objects of a bucket with {object_path} prefix     * (`recursive=true`) list content recursively     * (`all=true`) include hidden objects * (`stat=true`) get the meta of the object at {object_path} * (`sign=[GET,PUT,POST]`) fetch presigned urls to operate on {object_path}     * (`all=true`) allow link creation for hidden objects
        :param bucket_name: (required)
        :type bucket_name: str
        :param object_path: (required)
        :type object_path: str
        :param query: URL Query parameters.
        :type query: ListQuery | QueryParamTypes, optional
        :param query['stat'] (dict) <br> query.stat (Query) :
        :type query['stat']: bool
        :param query['recursive'] (dict) <br> query.recursive (Query) :
        :type query['recursive']: bool
        :param query['all'] (dict) <br> query.all (Query) :
        :type query['all']: bool
        :param query['start_after'] (dict) <br> query.start_after (Query) :
        :type query['start_after']: str
        :param query['fetch_content_type'] (dict) <br> query.fetch_content_type (Query) :
        :type query['fetch_content_type']: bool
        :param query['get_as_attachment'] (dict) <br> query.get_as_attachment (Query) :
        :type query['get_as_attachment']: bool
        :param query['max_keys'] (dict) <br> query.max_keys (Query) :
        :type query['max_keys']: int
        :param query['sign'] (dict) <br> query.sign (Query) :
        :type query['sign']: str
        :param query['store'] (dict) <br> query.store (Query) :
        :type query['store']: str
        :param query['expiry_days'] (dict) <br> query.expiry_days (Query) :
        :type query['expiry_days']: int
        :param query['expiry_hours'] (dict) <br> query.expiry_hours (Query) :
        :type query['expiry_hours']: int
        :param query['expiry_seconds'] (dict) <br> query.expiry_seconds (Query) :
        :type query['expiry_seconds']: int
        :param query['content_length_min'] (dict) <br> query.content_length_min (Query) :
        :type query['content_length_min']: int
        :param query['content_length_max'] (dict) <br> query.content_length_max (Query) :
        :type query['content_length_max']: int
        :param query['content_type'] (dict) <br> query.content_type (Query) :
        :type query['content_type']: str
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "bucket_name": str(bucket_name),
            "object_path": str(object_path),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(ListQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": ResponseList if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "422": HTTPValidationError,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/storage/v1/bucket/{bucket_name}/{object_path}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def remove(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: RemoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> HALEntity: ...

    @overload
    async def remove(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: RemoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def remove(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: RemoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def remove(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: RemoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def remove(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: RemoveQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def remove(
        self,
        bucket_name: StrictStr,
        object_path: StrictStr,
        *,
        query: RemoveQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> HALEntity | T | Response | Model:
        """Remove Object Or Folder.

        Remove the object or folder at {object_path}.  An {object_path} ending in a `/` requests folder deletion of an empty folder unless: * (`recursive=true`) forces recursive deletion of a (non-empty) folder. * (`all=true`) forces recursive deletion, including hidden objects.
        :param bucket_name: (required)
        :type bucket_name: str
        :param object_path: (required)
        :type object_path: str
        :param query: URL Query parameters.
        :type query: RemoveQuery | QueryParamTypes, optional
        :param query['recursive'] (dict) <br> query.recursive (Query) :
        :type query['recursive']: bool
        :param query['all'] (dict) <br> query.all (Query) :
        :type query['all']: bool
        :param query['start_after'] (dict) <br> query.start_after (Query) :
        :type query['start_after']: str
        :param query['max_keys'] (dict) <br> query.max_keys (Query) :
        :type query['max_keys']: int
        :param query['store'] (dict) <br> query.store (Query) :
        :type query['store']: str
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        # path parameters
        path_params: Dict[str, str] = {
            "bucket_name": str(bucket_name),
            "object_path": str(object_path),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(RemoveQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": HALEntity if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "422": HTTPValidationError,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="DELETE",
            resource_path="/storage/v1/bucket/{bucket_name}/{object_path}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )
