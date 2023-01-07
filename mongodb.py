import pymongo
client = pymongo.MongoClient(host='localhost', port=12306)
db = client.test
collection = db.students
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)
# results = collection.find_one({'age':{'$in':[20,23]}})
condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
