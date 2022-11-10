from pymongo import MongoClient


def get_database():
  CONNECTION_STRING = "mongodb://localhost:27017/"
  client = MongoClient(CONNECTION_STRING)
  return client['julie']['me']

def insert(key, val):
  me = get_database()
  me.insert_one({key:val})

def remember(val):
  results = []
  julie = get_database()
  query = julie.find({val:{"$exists":True}},{"_id": 0})
  for item in query:
    results.append(item[val])
  return results
