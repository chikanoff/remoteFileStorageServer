from flask_restx import Namespace, Resource, fields
from conduit.models.file import File

ns = Namespace("files", path="/files")

user_model = ns.model("User", {"username": fields.String, "role": fields.String, "first_name": fields.String})
file_model = ns.model(
    "File",
    {
        "name": fields.String,
        "description": fields.String,
        "mode": fields.String,
        "id": fields.Integer,
        "owner_id": fields.Integer,
        "owner": fields.Nested(user_model),
    },
)


@ns.route("/adminFiles")
class getAdminFiles(Resource):
    @ns.marshal_list_with(file_model)
    def get(self):
        files = File.getAdminFiles()
        return files


@ns.route("/all")
class getPublicFiles(Resource):
    @ns.marshal_list_with(file_model)
    def get(self):
        files = File.getPublicFiles()
        return files


@ns.route("/<int:file_id>")
class getOne(Resource):
    @ns.marshal_with(file_model)
    def get(self, file_id):
        file = File.getOne(file_id)
        return file

@ns.route("/filesFromUser/<int:user_id>")
class getFilesFromUser(Resource):
    def get(self, user_id):
        files = File.getUserFiles(user_id)
        return files

