from flask_socketio import emit
from conduit.extensions import socketio
from conduit.models.file import File
from conduit.models.user import User
from conduit.utils import get_jwt_identity_from_cookies
import os
import uuid

@socketio.on('get_file')
def get_file(data):
    ROOT_DIR = os.path.abspath(os.curdir) + "\\"
    file = File.get_by_id(data["data"])
    path = file.path
    ext = path.split(".")[-1]

    with open(ROOT_DIR + path.replace("/", "\\"), 'rb') as f:
        buf = f.read()
    print(buf)
    emit('your-file', {'data': buf, 'ext': "." + ext, 'name': file.name})

@socketio.on('upload-file')
def upload_file(data):
    print(data["desc"])
    ROOT_DIR = os.path.abspath(os.curdir) + "\\"
    owner_id = User.get_by_username(get_jwt_identity_from_cookies()).id
    path = "storage/" + str(uuid.uuid4()) + "." + data["ext"]
    File.create(data["name"], data["desc"], data["isPriv"], path, owner_id)
    with open(ROOT_DIR + path.replace("/", "\\"), 'wb') as f:
        f.write(data["buf"])
