from flask import Flask, request, abort
import functools
import jwt
from flask import current_app
from app.models.user_model import User


def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        try:
            decoded = jwt.decode(token, key=current_app.config['SECRET_KEY'], algorithms='HS256')
            id = decoded['id']
            username = decoded['username']
            user = User(id=id, username=username)
        except jwt.DecodeError:
            abort(400, message='Token is not valid.')
        except jwt.ExpiredSignatureError:
            abort(400, message='Token is expired.')
        return method(user, *args, **kwargs)

    return wrapper
