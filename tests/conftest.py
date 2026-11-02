import pytest_asyncio

from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import NullPool

from app.core.config import settings
from app.db.session import get_session
from app.main import app


@pytest_asyncio.fixture
async def db_session() -> AsyncSession:
    """
    Creates an AsyncSession wrapped in a transaction that is rolled back
    after each test, so tests never leave data behind.

    Commits made by the code under test become savepoints inside that
    transaction. A dedicated unpooled engine keeps connections from being
    shared across event loops.
    """

    engine = create_async_engine(settings.database_url, poolclass=NullPool)

    async with engine.connect() as connection:
        transaction = await connection.begin()

        session = AsyncSession(
            bind=connection,
            expire_on_commit=False,
            join_transaction_mode="create_savepoint",
        )

        try:
            yield session
        finally:
            await session.close()
            await transaction.rollback()

    await engine.dispose()


@pytest_asyncio.fixture
async def client(db_session: AsyncSession) -> AsyncClient:
    """
    HTTP client for API tests. Requests share the test's rolled-back session.
    """

    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client

    app.dependency_overrides.clear()
