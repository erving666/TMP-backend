import db
import inject
from flask import Flask
from app.repositorys import UserRepository
from app.services import UserService
from config import Config

db.init_db()


def config_ioc(binder):
    user_repository = UserRepository()

    user_service = UserService()

    binder.bind(UserRepository, user_repository)

    binder.bind(UserService, user_service)


def create_app():
    inject.configure(config_ioc)
    app = Flask(__name__)
    app.config.from_object(Config)
    return app
