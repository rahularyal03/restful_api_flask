import os
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
db = MongoClient(os.getenv("MONGODB_URI"),
                 authSource='admin',
                 maxPoolSize=50,
                 wtimeoutMS=2500)["Rest_Api"]