from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    return client['access_control_system']

def get_users_collection(db):
    return db['users']

def get_organisations_collection(db):
    return db['organisations']

def get_permissions_collection(db):
    return db['permissions']
