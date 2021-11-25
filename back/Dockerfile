FROM python:3.9.9-slim

EXPOSE 8080

RUN pip install --update pip && \
    pip install pipenv

COPY Pipfile* ./

RUN pipenv sync --system

COPY main.py bookclub migrations logcfg.yaml ./

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--log-config", "logcfg.yaml"]
