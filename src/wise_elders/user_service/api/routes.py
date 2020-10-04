from aiohttp import web
from wise_elders.user_service.api import api


def init_routes(app: web.Application):
    app.add_routes([
        web.get('/api/ping', api.ping)
    ])
