from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str

    class Config:
        orm_mode = True

class Organisation(BaseModel):
    name: str

    class Config:
        orm_mode = True


from enum import Enum

class AccessLevel(str, Enum):
    read = "READ"
    write = "WRITE"
    admin = "ADMIN"

class Permission(BaseModel):
    user_id: str
    org_name: str
    access_level: AccessLevel
