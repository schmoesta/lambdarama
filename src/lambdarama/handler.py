# SPDX-FileCopyrightText: 2024-present schmoesta <goestavg@gmail.com>
#
# SPDX-License-Identifier: MIT

from mangum import Mangum

from .app import app

handler = Mangum(app)
