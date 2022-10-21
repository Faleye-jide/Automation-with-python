import os


db_name = os.environ.get('DB_NAME')
db_password = os.environ.get('DB_PASS')

print(db_name, db_password)