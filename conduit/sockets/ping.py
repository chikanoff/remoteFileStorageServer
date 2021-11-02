from loguru import logger
from flask import request
from flask_socketio import emit
from conduit.extensions import socketio
from conduit.utils import get_jwt_identity_from_cookies, login_required


@socketio.on("connect")
def connect(data):
    identity = get_jwt_identity_from_cookies()
    print("identity", identity)
    emit("welcome", {"name": "mee"})


@socketio.event
@login_required
def message(data):
    print("message", data)
    emit("message", data)
