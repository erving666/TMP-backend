from app.api import user


def init(app):
    app.register_blueprint(user, url_prefix='/user')
