from aclook import aclook_api


def init_app(app):

    from modules import bird
    aclook_api.add_namespace(bird.api)
