from contextlib import asynccontextmanager
from typing import AsyncGenerator

from beanie import init_beanie
from fastapi import FastAPI
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from api.db.models import load_all_models
from api.settings import settings


async def _setup_db(app: FastAPI) -> None:
    logger.info("Setting up database")

    client = AsyncIOMotorClient(
        str(settings.db_url), uuidRepresentation="standard",
    )  # type: ignore
    app.state.db_client = client
    await init_beanie(
        database=client[settings.db_base],
        document_models=load_all_models(),
        # type: ignore
    )


@asynccontextmanager
async def lifespan_setup(
    app: FastAPI,
) -> AsyncGenerator[None, None]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    in the state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    app.middleware_stack = None
    await _setup_db(app)
    app.middleware_stack = app.build_middleware_stack()

    yield
