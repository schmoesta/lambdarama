# SPDX-FileCopyrightText: 2024-present schmoesta <goestavg@gmail.com>
#
# SPDX-License-Identifier: MIT


from logging import Logger

from fastapi import FastAPI, Request
from pydantic import BaseModel

from .__about__ import __description__ as app_description
from .__about__ import __name__ as app_name
from .__about__ import __version__ as app_version
from .config import get_config

config = get_config()

app = FastAPI(title="LambdaRama", version=app_version)

logger = Logger("root", config.log_level)


class ApiInfo(BaseModel):
    name: str
    version: str
    description: str
    docs_url: str | None
    build: str | None


@app.get("/", summary="Return API Info")
def root(request: Request) -> ApiInfo:
    logger.debug(str(request))
    return ApiInfo(
        name=app_name,
        version=app_version,
        description=app_description,
        docs_url=app.docs_url,
        build=config.build,
    )
