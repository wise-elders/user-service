from aiohttp import web


async def ping(req: web.Request) -> web.Response:
    return web.json_response({'message': 'pong'})
