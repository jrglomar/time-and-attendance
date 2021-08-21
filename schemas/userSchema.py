
from datetime import datetime as dt
from pydantic import BaseModel
from typing import List, Optional
from schemas.userTypeSchema import UserType

class UserBase(BaseModel):
    user_type_id: Optional[str] = None
    email: str
    password: str

# Schema for request body
class CreateUser(UserBase):
    pass

# Schema for response body
class User(BaseModel):
    created_at: dt
    updated_at: dt
    