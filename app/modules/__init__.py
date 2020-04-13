from aclook import api


def init_app(app):

    from modules import bird
    api.add_namespace(bird.api)
