from flask_socketio import emit
from conduit.extensions import socketio
from conduit.models.file import File
import os

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
    name = data["name"]
    print(name)

