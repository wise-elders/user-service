import asyncio
import pytest

from wise_elders.user_service.main import create_application as api_app


@pytest.fixture(autouse=True)
def loop():
    return asyncio.get_event_loop()


@pytest.fixture
async def client(aiohttp_client):
    return await aiohttp_client(api_app())
