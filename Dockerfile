FROM python:3.8.5 as base

WORKDIR /app
RUN apt-get -y update
RUN apt-get -y install curl 
ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
COPY poetry.toml .
COPY pyproject.toml .
RUN poetry install
COPY todo_app todo_app


FROM base as production
ENTRYPOINT [ "poetry", "run", "gunicorn", "-b", "0.0.0.0:8080", "todo_app.app:app"]


FROM base as development
ENTRYPOINT [ "poetry", "run", "flask", "run", "-h", "0.0.0.0"]

