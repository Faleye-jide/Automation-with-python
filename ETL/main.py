
from pymongo import MongoClient
from bson.objectid import ObjectId

password = '4LWzVfsZ46PWzmc5'
cluster = f"mongodb+srv://Jaymoney:{password}@cluster0.7ztfwpx.mongodb.net/test?retryWrites=true&w=majority"


client = MongoClient(cluster)


# print(client.list_database_names())


# use test database
mydb = client.test

# add data to the collection 

# employee1 ={
#     'name': "jide",
#     "age": 28,
#     "gender":"Male"
# }

# # add the data to the database
# employee = mydb.employee

# # inserting one item
# result = employee.insert_one(employee1)

# employee2 = [
#     {
#     'name': "Busayo",
#     "age": 19,
#     "gender":"Female"
#     },
#     {
#     'name': "Alex",
#     "age": 23,
#     "gender":"Male"
#     }
# ]

# # add multiple data to the db
# result = employee.insert_many(employee2)

# To perform any operation on the collection, you need to use the collection instance
mycol = mydb.employee




"""
To perform any operation on the collection, you need to use the collection instance
To query data, we can use Find and Find_one method.
Find returns an iterable objects and find_one returns the first occurrence in the collection
    
"""
# to return the first occurrence in the collection
one_record = mycol.find_one()
# print(one_record)


# To find a specific data
query = {'name':'jide','gender':'Male'}
result = mycol.find(query)
# print(list(one_record))


# How to retrive ID
query = {'_id':ObjectId('638de70a29dab0053e4ae710')}
one_record = mycol.find(query)
# for data in one_record:
    # print(data)



# To count documents in our collection

# count = 0
# for data in list(result):
#     count += 1
# print(count)

# we can use the count the number of collections using count_documents method

res = mycol.count_documents({'gender':'Female'})
# print(res)


"""
------------------------GET OPERATION-----------------------
To perform any operation on the collection, you need to use the collection instance
To query data, we can use Find and Find_one method.
Find returns an iterable objects and find_one returns the first occurrence in the collection
    
"""

"""_summary_: Query in mongoDB
    To find data by specific fields
 """
age = 25

res = mycol.find({'age': {'$gte': age}})
# for data in list(res):
    # print(data)
    
    
"""_summary_
    To sort query 
    we can also sort by specific key or field 
    use sort()
    
"""
    
res = mycol.find({'age': {'$lt': age}}).sort('name')
# print(list(res))

res = mycol.find({'age': {'$lt': age}}).sort('name', -1) # to sort descending)
# print(list(res))
     
     
     
     
"""
--------------------DELETE OPERATION---------------------------
TO DO DELETE DOCUMENT FROM THE COLLECTION
- delete by id 
- delete all documents 
"""


# res = mycol.delete_one({'_id':ObjectId('638de70a29dab0053e4ae710')})

# all_delete = mycol.delete_many({}) # to delete all the documents in the collection


"""
----------UPDATE OPERATION----------------------------------
TO DO UPDATE DOCUMENT FROM THE COLLECTION
- update a field/key in a document
"""


# res = mycol.update_one({'name':'jide'}, {'$set':{'age':30}}) # to update a single field in a document 


"""
----------LIMIT OPERATION----------------------------------
TO restrict the number of returned documents
"""

res = mycol.find({'name': 'jide'}).limit(1)

print(list(res))
# add another database to the server 
# mydb2 = client.myDatabase
# new_col = mydb['customers']

# print(client.list_database_names())

# mydb2 = client.myDatabase
# print('Database created............')

# print(client.list_database_names())
