from pymongo import MongoClient
url = 'mongodb+srv://admin:admin@cluster0.c9z0ut1.mongodb.net/pytech',
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)