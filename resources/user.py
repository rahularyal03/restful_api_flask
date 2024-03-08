from flask_restful import Resource, reqparse
from models.user import UserModel
from flask import jsonify

class User(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type = str,
                        required = True,
                        help = "This field cannot be empty"
                        )
    parser.add_argument('email',
                        type = str,
                        required = True,
                        help = "This field cannot be empty"
                        )
    parser.add_argument('phone',
                        type = str,
                        required = True,
                        help = "This field cannot be empty"
                        )
    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = "This field cannot be empty"
                        )
        
    def post(self):
        data = User.parser.parse_args()
        res = UserModel(data)
        result = res.save_to_db()
        return data, 201
        
   
    def get(self):
        users=[]
        data = UserModel.get_all_users()
        if data is not None:
            for obj in data:
                obj["_id"] = str(obj["_id"])
                users.append(obj)

            return jsonify(users)
        return {'message': 'Data not found.'}, 204