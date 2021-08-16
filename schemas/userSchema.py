from datetime import datetime as dt
from pydantic import BaseModel

class UserBase(BaseModel):
    user_type_id: int
    email: str
    password: str

# Schema for request body
class CreateUser(UserBase):
    pass

# Schema for response body
class User(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt