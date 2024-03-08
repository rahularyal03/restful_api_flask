from flask import Flask
from flask_restful import Api
from resources.user import User
from resources.parent import Parent
from resources.child import Child

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user')
api.add_resource(Parent, '/parent')
api.add_resource(Child, '/child')
      
if __name__ == '__main__':
    app.run(debug=True)