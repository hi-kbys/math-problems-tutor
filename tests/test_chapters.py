import pytest_asyncio
import pytest
from httpx import AsyncClient
import starlette.status

from tests.test_utils import async_client
    
@pytest.mark.asyncio
async def test_create_and_read(async_client: AsyncClient):
    # post
    response = await async_client.post(
        "/units",
        json={"title": "ベクトル", "school_year": 2},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # read_all
    response = await async_client.get("/units")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json[0]["title"] == "ベクトル"
    assert response_json[0]["school_year"] == 2

@pytest.mark.asyncio
async def test_create_and_read_with_id(async_client: AsyncClient):
    # post
    response = await async_client.post(
        "/units",
        json={"title": "微分", "school_year": 2},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # read problem with_id 1
    response = await async_client.get("/units/1")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json["title"] == "微分"
    assert response_json["school_year"] == 2

@pytest.mark.asyncio
async def test_update(async_client: AsyncClient):
    # post
    response = await async_client.post(
        "/units",
        json={"title": "微分", "school_year": 2},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # update
    # read problem with_id 1
    response = await async_client.get("/units/1")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json["title"] == "微分"
    assert response_json["school_year"] == 2
    
    response = await async_client.put(
        "/units/1",
        json={"title": "積分", "school_year": 2},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    response_json = response.json()
    assert response_json["title"] == "積分"
    assert response_json["school_year"] == 2

@pytest.mark.asyncio
async def test_delete(async_client: AsyncClient):
    # post
    response = await async_client.post(
        "/units",
        json={"title": "微分", "school_year": 2},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    
    # delete
    response = await async_client.delete("/units/1")
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json() is None
    