from datetime import datetime as dt
from pydantic import BaseModel

class UserProfileBase(BaseModel):
    user_id: int
    first_name: str
    last_name: str

# Schema for request body
class CreateUserProfile(UserProfileBase):
    pass

# Schema for response body
class UserProfile(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt