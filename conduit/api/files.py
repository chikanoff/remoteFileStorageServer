from flask import request, make_response
from flask_restx import Namespace, Resource
from conduit.models.file import File
from conduit.app import db

ns = Namespace("files", path="/files")

@ns.route("/")
class getPublicFiles(Resource):
    def get(self):
        files = File.getPublicFiles()
        return files

@ns.route("/<int:file_id>")
class getOne(Resource):
    def get(self, file_id):
        file = File.getOne(file_id)
        return file
        

