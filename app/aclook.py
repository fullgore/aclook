from flask import Blueprint
from flask_restplus import Api
from dependency_injector import containers, providers

from utils.ACBirdCommand import ACBirdCommand

aclook_api = Api(
    version='1.0',
    title="Bird Looking glass",
    description="Some description",
)


def init_app(app):
    aclook_api_blueprint = Blueprint('api', __name__, url_prefix='/api/')
    aclook_api.init_app(app)
    app.register_blueprint(aclook_api_blueprint)


class AppServiceContainer(containers.DeclarativeContainer):
    bird_socket = providers.Dependency(instance_of=str)
    bird_cmd = providers.Factory(ACBirdCommand, socket_file=bird_socket)


appSC = AppServiceContainer()
