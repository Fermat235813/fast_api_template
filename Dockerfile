######################################################################
                      #Base Stage
######################################################################

# Base image
FROM python:3.13.1-slim as base

# install poetry
RUN pip install poetry

#set work directory
WORKDIR /app
COPY . .

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi --no-dev

# run uvicorn
RUN pip install fastapi uvicorn pydantic-settings python-decouple


######################################################################
                      #Test Stage
######################################################################

# test image
FROM base as test

COPY tests tests/
RUN poetry install --no-interaction --no-ansi

# run tests
CMD poetry run pytest tests --color=yes


######################################################################
                      #Production Stage
######################################################################

# smal image
FROM base as production

# run app
CMD uvicorn app.main:app --host 0.0.0.0
