"""Automatic pytest fixtures."""

import random

import httpx
import pytest
import starlette.requests as req
import starlette.responses as res
from waylay.sdk import ApiClient, WaylayClient, WaylayConfig
from waylay.sdk.auth import NoCredentials
from waylay.services.storage.service import StorageService

random.seed(10)
GATEWAY_URL = "http://example.io"


@pytest.fixture(name="gateway_url")
def fixture_gateway_url() -> str:
    return GATEWAY_URL


@pytest.fixture(name="waylay_config")
def fixture_config(gateway_url) -> WaylayConfig:
    return WaylayConfig(credentials=NoCredentials(gateway_url=gateway_url))


@pytest.fixture(name="waylay_api_client")
def fixture_api_client(waylay_config: WaylayConfig) -> ApiClient:
    return ApiClient(waylay_config, {"auth": None})


@pytest.fixture(name="service")
def fixture_service(waylay_api_client: ApiClient) -> StorageService:
    return StorageService(waylay_api_client)


@pytest.fixture(name="waylay_client")
def fixture_waylay_client(waylay_config: WaylayConfig) -> WaylayClient:
    return WaylayClient(waylay_config, {"auth": None})


@pytest.fixture(name="test_app", scope="module")
def fixture_my_app():
    async def echo_app(scope, receive, send):
        request = req.Request(scope, receive)
        content_type = request.headers.get("content-type", "application/octet-stream")
        if content_type.startswith("application/json"):
            response = res.JSONResponse(await request.json())
        elif content_type.startswith("multipart/form-data") or content_type.startswith(
            "application/x-www-form-urlencoded"
        ):
            form = await request.form()
            response = res.JSONResponse({
                key: (value if isinstance(value, str) else {"size": value.size})
                for key, value in form.items()
            })
        else:
            bytes = await request.body()
            response = res.JSONResponse({"bytes": str(bytes, encoding="utf-8")})
        await response(scope, receive, send)

    return echo_app


@pytest.fixture(name="echo_service")
async def fixture_echo_client(service, test_app):
    async with service({
        "transport": httpx.ASGITransport(test_app),
        "auth": None,
    }) as srv:
        yield srv
