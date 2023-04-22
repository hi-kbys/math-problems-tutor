import pytest_asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import starlette.status

from mpt_app.main import app
from mpt_app.db import Base, get_db

ASYNC_DB_URL = "sqllite+aiosqlite:///:memory:"

@pytest_asyncio.fixture
async def async_client():
    # Create AsyncEngine
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )

    # Create tables
    async with async_session.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # DB dependency
    async def get_test_db() -> AsyncSession:
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
    
@pytest.mark.asyncio
async def test_create_and_read(async_client: AsyncClient):
    response = await async_client.post(
        "/problems",
        json={}
    )