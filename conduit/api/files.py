from flask import request, make_response, jsonify
from flask_restx import Namespace, Resource, fields
from conduit.models.file import File
from conduit.app import db

ns = Namespace("files", path="/files")

@ns.route("/getAll")
class getAll(Resource):
    def get(self):
        files = File.getAll()
        response = make_response({'files': files})
        return response
