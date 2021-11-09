from flask import request, make_response
from flask_restx import Namespace, Resource
from conduit.models.file import File
from conduit.app import db

ns = Namespace("files", path="/files")

@ns.route("/getAll")
class getAll(Resource):
    def get(self):
        files = File.getAll()
        response = make_response({"status": "success", "files": files})
        return response
