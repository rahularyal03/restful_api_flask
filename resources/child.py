from flask_restful import Resource, reqparse
from models.child  import ChildModel

class Child(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument("type",
                       type = str,
                       required=True,
                       help="This field can't be empty"
                       )
    parse.add_argument("model",
                       type = str,
                       required=True,
                       help="This field can't be empty"
                       )
    
    def post(self):
        data = Child.parse.parse_args()
        res = ChildModel(data)
        data = res.save_to_db()
        print(data)
        for obj in data:
            print("Hello")
            print(obj)
        return "Child added Successfully"