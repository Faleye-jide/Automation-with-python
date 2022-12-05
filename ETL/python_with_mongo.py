import pymongo

# connect to default database
local_host = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(local_host)

# create a database in mongodb server
mydb = client['Employee']

# list all the database in the server
db_list = client.list_database_names()
if mydb in db_list:
    print('It exist')