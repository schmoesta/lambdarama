# LambdaRama

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

This project is a starter for creating serverless HTTP APIs on AWS Lambda. Here are some of it's key features:

- built with the excellent [FastAPI](https://fastapi.tiangolo.com/) framework
- uses the [Mangum](https://mangum.io/) ASGI adapter for AWS Lambda
- leverages the [Docker runtime](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html), because who really wants to mess around with Lambda layers and .zip-files?
- project management with [hatch](https://hatch.pypa.io/1.9/)
- opinionated, strict and automatic enforcement of code style - less room to argue, more time to be productive

---

**Table of Contents**

- [🏗️ Setup](#🏗️-setup)
- [🗂️ Project Structure](#🗂️-project-structure)
- [🫶 Contributing](#🫶-contributing)
- [⚖️ License](#⚖️-license)

## 🏗️ Setup

This project is managed by [hatch](https://hatch.pypa.io/1.9/) - follow the instructions [here](https://hatch.pypa.io/1.9/install/) for setting up hatch on your machine. This project requires you to have Python >=3.8 available.

```bash
hatch run dev:test
```

### Environments

This project provides two [environments](https://hatch.pypa.io/1.9/environment/):

- `default`: This one has only the runtime dependencies of the lambda function.
- `dev`: This one is used for local development, adding dev-dependencies like `ruff`, `mypy`, `pytest`, etc.

## 🗂️ Project Structure

todo: explain project structure

### 📜 Scripts

There are a number of [scripts]() available to perform common develpment tasks. They are defined for the `dev` environment and can be invoked by running: `hatch run dev:<name of script>`, e.g. `hatch run dev:lint`.

| Script                       | Description                                   |
| ---------------------------- | --------------------------------------------- |
| `hatch run dev:lint-style`   | Lint code style with `ruff`                   |
| `hatch run dev:lint-format`  | Lint code format with `ruff`                  |
| `hatch run dev:lint-types`   | Lint types with `mypy`                        |
| `hatch run dev:lint-commits` | Lint commits with `gitlint`                   |
| `hatch run dev:lint-all`     | Perform all linting tasks                     |
| `hatch run dev:format`       | Format code with `ruff`                       |
| `hatch run dev:test`         | Run tests with `pytest`                       |
| `hatch run dev:cov`          | Get `coverage` report                         |
| `hatch run dev:serve`        | Start hot reloading dev server with `uvicorn` |

## 🫶 Contributing

Please refer to the [CONTRIBUTING.md](./CONTRIBUTING.md) document to see how to contribute to this project.

## ⚖️ License

`lambdarama` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
