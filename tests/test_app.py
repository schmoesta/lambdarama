# SPDX-FileCopyrightText: 2024-present schmoesta <goestavg@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Any

from fastapi.testclient import TestClient
from lambdarama.__about__ import __description__ as app_description
from lambdarama.__about__ import __name__ as app_name
from lambdarama.__about__ import __version__ as app_version
from lambdarama.app import ApiInfo, app

client = TestClient(app)


def test_app_root():
    response = client.get("/")
    body: dict[str, Any] = response.json()
    api_info = ApiInfo(**body)
    assert response.status_code == 200
    assert api_info.name == app_name
    assert api_info.description == app_description
    assert api_info.version == app_version
