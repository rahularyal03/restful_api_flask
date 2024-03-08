from db import db
from werkzeug.security import generate_password_hash

class UserModel(object):
    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.phone = data.get("phone")
        self.password = data.get("password")
        
    
    def get_name(self):
        return self.name
    
    def get_name(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_assword(self):
        return self.password
    
    def get_all_users():
        result = db.users.find({})
        if result:
             return result
        return None
    
    def save_to_db(self):
        data = db.users.update_one(
             {
                "email": self.email
            },
            {
                "$set": {
                    "name": self.name,
                    "phone": self.phone,
                    "password": generate_password_hash(self.password)
                },
                
            },
            upsert=True
        )
        return "User Added Successfully"
    
    
        