from flask_socketio import emit
from conduit.extensions import socketio
from conduit.utils import get_jwt_identity_from_cookies, login_required


@socketio.on("connect")
def connect(data):
    data = data | None  # fuck linter
    identity = get_jwt_identity_from_cookies()
    print("identity", identity)
    emit("welcome", {"name": "mee"})


@socketio.event
@login_required
def message(data):
    print("message", data)
    emit("message", data)
