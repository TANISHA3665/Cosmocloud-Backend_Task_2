from pymongo.collection import Collection
from models import Permission

def create_or_update_permission(perm: Permission, permissions_collection: Collection):
    query = {'user_id': perm.user_id, 'org_name': perm.org_name}
    update = {'$set': {'access_level': perm.access_level}}
    permissions_collection.update_one(query, update, upsert=True)

def remove_permission(perm: Permission, permissions_collection: Collection):
    query = {'user_id': perm.user_id, 'org_name': perm.org_name}
    permissions_collection.delete_one(query)
