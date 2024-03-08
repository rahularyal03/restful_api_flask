b = MongoClient(os.getenv("MONGO_URI"),
#                  authSource='admin',
#                  maxPoolSize=50,
#                  wtimeout=2500)['Rest_Api']