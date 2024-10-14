from http import HTTPStatus

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={
                    "error": "Client Error",
                    "message": str(http_exception.detail),
                },
            )
        except Exception as e:
            logger.error(str(e))
            return JSONResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content={
                    "error": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
                    "message": str(e),
                },
            )
