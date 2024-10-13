# OpenAI Assistants API Demo

This project was generated using [fastapi_template](https://github.com/s3rius/FastAPI-template).

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m api
```

This will start the server on the configured host.

You can find swagger documentation at `/v1/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker compose up --build -d
```

If you want to develop in docker with autoreload, add `-f docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d
```

This command mounts current directory and enables autoreload. You can access the application at `localhost/v1`

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker compose build
```

## Project structure

```bash
$ tree "api"
api
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifespan.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "DICOTA_" prefix.

For example if you see in your `api/settings.py` a variable named like `random_parameter`,
you should provide the `DICOTA_RANDOM_PARAMETER` variable to configure the value.
This behaviour can be changed by overriding `env_prefix` property in `api.settings.Settings.Config`.

```python
model_config = SettingsConfigDict(
    env_file=".env",
    env_prefix="DICOTA_",
    env_file_encoding="utf-8",
    extra = 'ignore'
)
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using `.pre-commit-config.yaml` file.

By default, it runs:
* black (formats your code);
* mypy (validates types);
* ruff (spots possible bugs);


You can read more about pre-commit here: https://pre-commit.com/
