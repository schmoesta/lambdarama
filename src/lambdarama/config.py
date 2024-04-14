# SPDX-FileCopyrightText: 2024-present schmoesta <goestavg@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    log_level: Literal[
        "CRITICAL",
        "FATAL",
        "ERROR",
        "WARN",
        "WARNING",
        "INFO",
        "DEBUG",
        "NOTSET",
    ] = Field("INFO")
    build: str | None = Field(None)


def get_config() -> Config:
    """get configuration from environment
    Returns:
        Config: configuration
    """
    # see https://github.com/pydantic/pydantic-settings/issues/201
    # for why disabling this rule here is necessary:
    return Config()  # type: ignore
