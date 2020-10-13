from aiohttp import web
from aiohttp_swagger import setup_swagger
from wise_elders.user_service.api.routes import init_routes
from wise_elders.user_service.api.errors import handle_error


def create_application():
    app = web.Application(middlewares=[
        handle_error
    ])
    init_routes(app)
    setup_swagger(
        app,
        title='Wise Elders User API',
        ui_version=3
    )
    return app


if __name__ == '__main__':
    web.run_app(app=create_application())
