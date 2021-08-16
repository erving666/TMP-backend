from app.api import user


def init(app):
    app.register_blueprint(user, url_prefix='/api/user')
    app.register_blueprint(info, url_prefix='/api/info')
