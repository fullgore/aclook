from flask import Blueprint
from flask_restplus import Api
from dependency_injector import containers, providers

from utils.ACBirdCommand import ACBirdCommand

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(
    api_blueprint,
    version='1.0b',
    title="Bird Looking glass",
    description="Get routes and attributs from bird daemon 2.x",
)


def init_app(app):
    app.register_blueprint(api_blueprint)


class AppServiceContainer(containers.DeclarativeContainer):
    bird_socket = providers.Dependency(instance_of=str)
    bird_timeout = providers.Dependency(instance_of=float)
    bird_cmd = providers.Factory(ACBirdCommand, socket_file=bird_socket, timeout=bird_timeout)


appSC = AppServiceContainer()
