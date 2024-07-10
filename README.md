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

**This is all still very much a work in progess. Please use at your own risk and expect things to break.**

---

**Table of Contents**

- [🏗️ Setup](#%EF%B8%8F-setup)
- [🗂️ Project Structure](#%EF%B8%8F-project-structure)
- [🫶 Contributing](#-contributing)
- [⚖️ License](#%EF%B8%8F-license)

## 🏗️ Setup

This project is managed by [hatch](https://hatch.pypa.io/1.9/) - follow the instructions [here](https://hatch.pypa.io/1.9/install/) for setting up hatch on your machine.

```bash
hatch run dev:test
```

### Environments

This project provides two [environments](https://hatch.pypa.io/1.9/environment/):

- `default`: This one has only the runtime dependencies of the lambda function.
- `dev`: This one is used for local development, adding dev-dependencies like `ruff`, `mypy`, `pytest`, etc.

### 🐙 CI with Github Actions

This project has Github Actions set up to build and push your Lambda function to ECR. If you want to fork the project to use it in the same way, have a look at these prerequisites. You need:

1. an ECR repository to push the images to. The workflow is set up to push to a repo that has the same name as the Github repo. You may however pass any other name to the [workflow](./.github/workflows/workflow_push_to_ecr.yml). Just add it as an optional input where the workflow is called.
2. an IAM role that Github Actions may assume via OIDC. Follow the [official documentation on Github](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) for how to set this up. Additionally the IAM role needs permission to push images to the ECR repository.
3. a couple of secrets set in your newly forked Github project:
   - `AWS_ACCOUNT_ID`: your AWS account ID.
   - `AWS_REGION`: the AWS region where your ECR repository is deployed.
   - `AWS_IAM_ROLE`: the IAM role to assume for pushing the image to ECR.

### 🙅‍♂️ Known Limitations

While the experience of using hatch has been very positive in most ways, it also comes with some drawbacks. There is still [no official support for lockfiles](https://hatch.pypa.io/1.12/meta/faq/#libraries-vs-applications), which is an important prerequisite for application development. The workaround for the moment is using the [pip-compile-plugin](https://github.com/juftin/hatch-pip-compile), which works well enough. Have a look at their documentation for how to use it, e.g. to [upgrade dependencies](https://github.com/juftin/hatch-pip-compile/blob/main/docs/upgrading.md).

## 🗂️ Project Structure

The project is organized the following way:

```
.
├── CONTRIBUTING.md
│     Instructions for contributing
├── Dockerfile
│     Dockerfile for the Lambda image
├── LICENSE.txt
│     License information
├── README.md
│      This readme
├── pyproject.toml
│     Project configuration
├── requirements
│   └── requirements-dev.txt
│         Dev requirements
├── requirements.txt
│     Production requirements
├── src
│   └── lambdarama
│       ├── __about__.py
│       │     Name, version and description
│       ├── __init__.py
│       ├── app.py
│       │     The actual FastAPI application
│       ├── config.py
│       │     Runtime configuration
│       └── handler.py
│             Mangum ASGI handler
└── tests
      Tests
```

### 📜 Scripts

There are a number of scripts available to perform common develpment tasks. They are defined for the `dev` environment and can be invoked by running: `hatch run dev:<name of script>`, e.g. `hatch run dev:lint`.

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
