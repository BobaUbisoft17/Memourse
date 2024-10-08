"""File to app middlewares."""

from typing import Awaitable, Callable

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from .auth.token_service import AuthJWT


class DatabaseMiddleware:
    """Middlware to transfer database session for endpoints."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def __call__(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        async with self.session() as session:
            request.state.session = session
            return await call_next(request)


class JWTMiddleware:
    """Middlware to transfer auth service for endpoints."""

    def __init__(self, jwt_service: AuthJWT) -> None:
        self.jwt_service = jwt_service

    async def __call__(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        request.state.jwt_service = self.jwt_service
        return await call_next(request)
