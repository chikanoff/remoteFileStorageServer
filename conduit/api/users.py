from flask_restx import Namespace, Resource, fields

from conduit.models.user import User


ns = Namespace("users")
user_model = ns.model("User", {"username": fields.String, "role": fields.String})


@ns.route("/<int:user_id>")
class UserById(Resource):
    @ns.marshal_with(user_model)
    def get(self, user_id):
        user = User.query.filter(User.query.filter_by(id=user_id).first_or_404())
        return user


@ns.route("/")
class UserList(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        users = User.query.all()
        return users
