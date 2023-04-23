from typing import Optional
from fastapi import Depends, FastAPI
from dependencies import get_users_collection, get_organisations_collection, get_permissions_collection
from models import Organisation, Permission, UserCreate
from users import create_user, list_users, get_user
from organisations import create_organisation, list_organisations
from permissions import create_or_update_permission, remove_permission

app = FastAPI()

@app.post("/users/")
async def create_new_user(user: UserCreate, users_collection = Depends(get_users_collection)):
    return create_user(user, users_collection)

@app.get("/users/")
async def list_all_users(name: Optional[str] = None, limit: int = 10, offset: int = 0, users_collection = Depends(get_users_collection)):
    return list_users(name, limit, offset, users_collection)

@app.get("/users/{user_id}")
async def fetch_single_user(user_id: str, users_collection = Depends(get_users_collection)):
    return get_user(user_id, users_collection)

@app.post("/organisations/")
async def create_new_organisation(org: Organisation, organisations_collection = Depends(get_organisations_collection)):
    return create_organisation(org, organisations_collection)

@app.get("/organisations/")
async def list_all_organisations(name: Optional[str] = None, limit: int = 10, offset: int = 0, organisations_collection = Depends(get_organisations_collection)):
    return list_organisations(name, limit, offset, organisations_collection)

@app.post("/permissions/")
async def create_or_update_permissions(perm: Permission, permissions_collection = Depends(get_permissions_collection)):
    return create_or_update_permission(perm, permissions_collection)

@app.delete("/permissions/")
async def remove_permissions(perm: Permission, permissions_collection = Depends(get_permissions_collection)):
    return remove_permission(perm, permissions_collection)
