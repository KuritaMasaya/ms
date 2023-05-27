from pymongo import MongoClient

client = MongoClient('')

db = client['']

mycollection = db[""]

one_record = mycollection.find()

for raw in one_record:
    print(raw)