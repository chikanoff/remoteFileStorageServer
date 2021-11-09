from flask_restx import Namespace, Resource
from conduit.models.file import File

ns = Namespace("files", path = "/files")

@ns.route("/adminFiles")
class getAdminFiles(Resource):
    def get(self):
        files = File.getAdminFiles()
        return files
        
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
