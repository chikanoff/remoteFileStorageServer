from flask import request, make_response, jsonify
from flask_restx import abort, Namespace, Resource, fields
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required
from loguru import logger
from conduit.utils import get_jwt_identity_from_cookies
from conduit.models.user import User
from conduit.app import db


ns = Namespace("auth", path="/auth")
user_data_model = ns.model(
    "LoginModel",
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "remember": fields.Boolean(required=False),
    },
    strict=True,
)
register_data_model = ns.model("RegisterModel", {
    "firstName": fields.String(required=True),
    "lastName": fields.String(required=True),
    "email": fields.String(required=True),
    "username": fields.String(required=True),
    "password": fields.String(required=True),
}, strict=True)


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
    @ns.response(500, "Internal server error")
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


@ns.route("/register")
class Register(Resource):
    @ns.expect(register_data_model)
    @ns.response(200, "New User was created successfully")
    @ns.response(400, "Wrong request")
    @ns.response(403, "Wrong username or password")
    @ns.response(500, "Internal server error")
    def post(self):
        first_name = request.json["firstName"]
        last_name = request.json["lastName"]
        email = request.json["email"]
        username = request.json["username"]
        password = request.json["password"]
        checks = User.check_username_and_email(
            username, email)
        if checks:
            response = jsonify(
                status="fail",
                message="Username or email already exist",
                errors=checks,
            )
            response.status_code = 403
            return response

        new_user = User.create(first_name, last_name,
                               email, username, password)
        db.session.add(new_user)
        db.session.commit()
        access_token = create_access_token(new_user.username)
        response = jsonify(
            status="success",
            message="successfully registered",
            access_token=access_token,
            token_type="bearer",
        )
        response.status_code = 200
        response.headers["Cache-Control"] = "no-store"
        response.headers["Pragma"] = "no-cache"

        return response
