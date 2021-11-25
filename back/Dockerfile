FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

EXPOSE 8080

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip && \
    pip install pipenv

COPY Pipfile* ./

RUN pipenv sync --system

COPY main.py bookclub migrations logcfg.yaml ./

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--log-config", "logcfg.yaml"]
