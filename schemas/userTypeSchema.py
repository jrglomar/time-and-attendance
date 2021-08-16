from datetime import datetime as dt
from pydantic import BaseModel

class UserTypeBase(BaseModel):
    title: str

# Schema for request body
class CreateUserType(UserTypeBase):
    pass

# Schema for response body
class UserType(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt