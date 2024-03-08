from flask_restful import reqparse,  Resource
from models.parent import ParentModel


class Parent(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('type',
                        type = str,
                        required = True,
                        help = "This field cannot be empty"
                        )
    parser.add_argument('make',
                        type = str,
                        required = True,
                        help = "This field cannot be empty"
                            )
    parser.add_argument('year',
                        type = str,
                        required = True,
                        help = "This field cannot be empty"
                        )
            
    def post(self):
        data = Parent.parser.parse_args()
        res = ParentModel(data)
        result = res.save_to_db()
        return result, 201
        