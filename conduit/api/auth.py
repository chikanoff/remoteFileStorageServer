from flask import request, make_response, jsonify
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required
from loguru import logger
from conduit.utils import get_jwt_identity_from_cookies
from conduit.models.user import User


ns = Namespace("auth", path="/auth")
user_data_model = ns.model(
    "UserData",
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "remember": fields.Boolean(required=False),
    },
    strict=True,
)


@ns.route("/isAuthenticated")
class IsAuthenticated(Resource):
    def get(self):
        identity = get_jwt_identity_from_cookies()
        # validte jwt TODO
        if identity:
            response = jsonify(is_authenticated=True, jwt_identity=identity)
            response.status_code = 200
            return response
        else:
            return jsonify(is_authenticated=False)


@ns.route("/login")
class Login(Resource):
    @ns.response(200, "Logged in successfully")
    @ns.response(400, "Wrong request")
    @ns.response(403, "Wrong username or password")
    @ns.expect(user_data_model, validate=True)
    def post(self):
        access_token = create_access_token("urer", fresh=True)
        response = make_response()
        response.status_code = 200
        username = request.json["username"]
        password = request.json["password"]
        remember = request.json["remember"]
        print(username, password, remember)
        set_access_cookies(response, access_token)
        return response
