from app.api import user
from app.api import info


def init(app):
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(info, url_prefix='/info')
