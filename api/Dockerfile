FROM python:3.12-slim 

WORKDIR /app

RUN apt-get update & apt-get install -y

RUN pip install poetry playwright

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction && poetry run playwright install

COPY . .
