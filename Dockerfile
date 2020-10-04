FROM python:3.8-slim as base
ENV PYTHONBUFFERED 1
WORKDIR user-service
COPY src/ .
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM base as test
COPY test .
COPY test-requirements.txt .
RUN pip install -r test-requirements.txt