from db import db
from bson import ObjectId

class ChildModel(object):
    def __init__(self, data):
        self.type = data.get('type')
        self.make = data.get('make')
        
    def save_to_db(self):
        data = db.childs.aggregate([
           {
               "$match": {"_id": ObjectId('65eb0fe6a08bb43d9d64ad0a')}
               
            },
           
            {
                "$lookup": {
                "from": "parents",
                "localField": "parentId",
                "foreignField": "_id",
                "as": "parentData"
            }},
            
            {"$unwind": "$parentData"},
            
            {
                "$project": {
                "_id": 1, 
                "type": self.type, 
                "model": self.make,
                "parentData.make": 1, 
                "parentData.year": 1 
            }}
        ])
        return data