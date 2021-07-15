import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',     # search for username in the json string
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )

    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field-p cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()  # use the parser whcih expects a username and parser

        if UserModel.find_by_username(data['username']):
            return {"message": "user already exists"}, 400  # NB if returned then following code not retunn

        user = UserModel(**data)    # same as data['username'], data['password'])
        user.save_to_db()

        return {"message":  "user created sucessfully"}, 201  # 'created' user response code
