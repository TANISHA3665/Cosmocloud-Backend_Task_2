from typing import Dict, List, Optional, Union
from fastapi import HTTPException
from pymongo.collection import Collection
from bson.objectid import ObjectId
from models import UserCreate, User

def create_user(user: UserCreate, users_collection: Collection) -> User:
    user_dict = user.dict()
    user_dict.pop('id', None)
    result = users_collection.insert_one(user_dict)
    user_dict['_id'] = str(result.inserted_id)
    return User(**user_dict)

def list_users(name: Optional[str], limit: int, offset: int, users_collection: Collection) -> Dict[str, Union[int, List[User]]]:
    query = {}
    if name:
        query['name'] = {'$regex': name}
    users = users_collection.find(query).skip(offset).limit(limit)
    total_count = users_collection.count_documents(query)
    return {'total_count': total_count, 'users': [User(**u) for u in users]}

def get_user(user_id: str, users_collection: Collection) -> User:
    user = users_collection.find_one({'_id': ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)
