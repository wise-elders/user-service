from aiohttp_swagger import swagger_path
from aiohttp import web


@swagger_path('/swagger/ping.yaml')
async def ping(req: web.Request) -> web.Response:
    return web.json_response({'message': 'pong'})
