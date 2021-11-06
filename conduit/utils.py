from flask import request
from flask_jwt_extended.utils import decode_token
from jwt import ExpiredSignatureError
from loguru import logger
import functools


def get_jwt_from_cookies():
    jwt = request.cookies.get("access_token_cookie", None)
    return jwt


def get_jwt_identity_from_cookies():
    jwt = get_jwt_from_cookies()
    if jwt:
        try:
            decoded_token = decode_token(jwt)
            identity = decoded_token.get("sub")
            return identity
        except ExpiredSignatureError:
            logger.debug(f"Expired signature in token: {jwt}")
    return None


def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        redirect_func = kwargs.get("redirect_func", None)
        identity = get_jwt_identity_from_cookies()
        if identity is None:
            if redirect_func:
                return redirect_func()
            return
        return f(*args, **kwargs)

    return wrapper
