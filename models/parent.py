from db import db

class ParentModel(object):
    def __init__(self, data):
        self.type = data.get('type')
        self.make = data.get('make')
        self.year = data.get("year")
        
    def save_to_db(self):
        data = db.parents.update_one(
             {
                "type": self.type
            },
            {
                "$set": {
                    "make": self.make,
                    "year": self.year
                },
                
            },
            upsert=True
        )
        return "Parent Added Successfully"