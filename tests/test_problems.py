import pytest_asyncio
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import starlette.status

from mpt_app.main import app
from mpt_app.db.base import Base
from mpt_app.db.session import get_db

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture
async def async_client():
    # Create AsyncEngine
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )

    # Create tables
    async with async_engine.begin() as conn:
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
    # post
    response = await async_client.post(
        "/problems",
        json={"title": "test", "statement": "test_statement"},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # read_all
    response = await async_client.get("/problems")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json[0]["title"] == "test"
    assert response_json[0]["statement"] == "test_statement"

@pytest.mark.asyncio
async def test_create_and_read_with_id(async_client: AsyncClient):
    # post
    response = await async_client.post(
        "/problems",
        json={"title": "test", "statement": "test_statement"},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # read problem with_id 1
    response = await async_client.get("/problems/1")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json["title"] == "test"
    assert response_json["statement"] == "test_statement"

@pytest.mark.asyncio
async def test_update(async_client: AsyncClient):
    # post
    response = await async_client.post(
        "/problems",
        json={"title": "test", "statement": "test_statement"},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # update
    response = await async_client.get("/problems")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json[0]["title"] == "test"
    assert response_json[0]["statement"] == "test_statement"
    assert response_json[0]["is_solved"] == False
    
    response = await async_client.put(
        "/problems/1",
        json={"title": "test_1", "statement": "test_statement_1", "is_solved": True},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json["title"] == "test_1"
    assert response_json["statement"] == "test_statement_1"

@pytest.mark.asyncio
async def test_delete(async_client: AsyncClient):
    # post
    response = await async_client.post(
        "/problems",
        json={"title": "test", "statement": "test_statement"},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # delete
    response = await async_client.delete("/problems/1")
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json() is None