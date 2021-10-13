from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('userName',
                        type=str,
                        required=True,
                        help="userName cannot be blank"
    )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password cannot be empty"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['userName']):
            return {"message": "{} useralready exists".format(data['userName'])}, 400
        
        user = UserModel(data['userName'], data['password'])
        user.save_to_db()

        return {"message": "{} registered successfully".format(data['userName'])}, 201