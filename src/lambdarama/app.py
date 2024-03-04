# SPDX-FileCopyrightText: 2024-present schmoesta <goestavg@gmail.com>
#
# SPDX-License-Identifier: MIT


from logging import Logger

from fastapi import FastAPI, Request

from .__about__ import __version__ as app_version
from .config import get_config

config = get_config()

app = FastAPI(title="LambdaRama", version=app_version)

logger = Logger("root", config.log_level)


@app.get("/")
def root(request: Request) -> dict[str, str]:
    logger.error("called / route:")
    return {"message": "Hello World"}
