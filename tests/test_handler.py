# SPDX-FileCopyrightText: 2024-present schmoesta <goestavg@gmail.com>
#
# SPDX-License-Identifier: MIT

from json import loads
from typing import Any
from unittest.mock import MagicMock

from mangum.types import LambdaContext, LambdaEvent
from pytest import fixture

from src.lambdarama.__about__ import __description__ as app_description
from src.lambdarama.__about__ import __name__ as app_name
from src.lambdarama.__about__ import __version__ as app_version
from src.lambdarama.app import ApiInfo
from src.lambdarama.handler import handler


@fixture
def api_gateway_event() -> LambdaEvent:
    return {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/my/path",
        "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
        "cookies": ["cookie1", "cookie2"],
        "headers": {"header1": "value1", "header2": "value1,value2"},
        "queryStringParameters": {"parameter1": "value1,value2", "parameter2": "value"},
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "api-id",
            "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                        "notBefore": "May 28 12:30:02 2019 GMT",
                        "notAfter": "Aug  5 09:36:04 2021 GMT",
                    },
                }
            },
            "authorizer": {
                "jwt": {
                    "claims": {"claim1": "value1", "claim2": "value2"},
                    "scopes": ["scope1", "scope2"],
                }
            },
            "domainName": "id.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "id",
            "http": {
                "method": "GET",
                "path": "/",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.0.2.1",
                "userAgent": "agent",
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390,
        },
        "body": "Hello from Lambda",
        "pathParameters": {"parameter1": "value1"},
        "isBase64Encoded": False,
        "stageVariables": {"stageVariable1": "value1", "stageVariable2": "value2"},
    }


def test_hander(api_gateway_event):
    response: dict[str, Any] = handler(api_gateway_event, MagicMock(spec=LambdaContext))
    body: dict[str, Any] = loads(response["body"])
    api_info = ApiInfo(**body)
    assert response["statusCode"] == 200
    assert api_info.name == app_name
    assert api_info.description == app_description
    assert api_info.version == app_version
