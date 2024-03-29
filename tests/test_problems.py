import pytest_asyncio
import pytest
from httpx import AsyncClient
import starlette.status

from tests.test_utils import async_client
    
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
    