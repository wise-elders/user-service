from aiohttp import web


@web.middleware
async def handle_error(request, handler):
    try:
        return await handler(request)
    except Exception as e:
        return web.json_response({'message': str(e)}, status=getattr(e, 'status', 500))
