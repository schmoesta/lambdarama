ARG PYTHON_VERSION=3.10
ARG HATCH_VERSION=1.9

FROM public.ecr.aws/lambda/python:${PYTHON_VERSION} AS base

FROM base AS builder
ARG PYTHON_VERSION
ARG HATCH_VERSION

WORKDIR /build

RUN pip3 install hatch~=${HATCH_VERSION}

COPY . /build

RUN hatch build -t wheel

FROM base AS deps

WORKDIR /deps

COPY requirements.txt  /tmp/requirements.txt
RUN  pip3 install -r /tmp/requirements.txt --target .

COPY --from=builder /build/dist/* /tmp/
RUN  pip3 install /tmp/*.whl --target .

FROM base as production

COPY --from=deps /deps/ ${LAMBDA_TASK_ROOT}/

CMD [ "lambdarama.handler" ]
