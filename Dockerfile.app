#fastapi + uvicornでのアプリの実行
FROM python:3.11-slim-buster

WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY poetry.lock* pyproject.toml* ./
RUN poetry install --no-root --no-dev
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "mpt_app.main:app", "--host", "0.0.0.0", "--reload"]