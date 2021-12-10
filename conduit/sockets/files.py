import os
import uuid
from flask_socketio import emit
from conduit.extensions import socketio
from conduit.models.file import File
from conduit.models.user import User


@socketio.on("get_file")
def get_file(data):
    ROOT_DIR = os.path.abspath(os.curdir) + "/"
    file = File.get_by_id(data["data"])
    path = file.path
    ext = path.split(".")[-1]

    with open(ROOT_DIR + path, "rb") as f:
        buf = f.read()
    print(buf)
    emit("your-file", {"data": buf, "ext": "." + ext, "name": file.name})


@socketio.on("upload-file")
def upload_file(data):
    print(data["currUser"])
    ROOT_DIR = os.path.abspath(os.curdir) + "/"
    owner_id = User.get_by_username(data["currUser"]).id
    path = "storage/" + str(uuid.uuid4()) + "." + data["ext"]
    isPriv = "private" if data["isPriv"] else "public"
    File.create(data["name"], data["desc"], str(isPriv), path, owner_id)

    with open(ROOT_DIR + path, "wb") as f:
        f.write(data["buf"])
