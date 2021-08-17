from datetime import datetime as dt
from pydantic import BaseModel

class EmployeeBase(BaseModel):
    user_type_id: str
    user_profile_id: str

# Schema for request body
class CreateEmployee(EmployeeBase):
    pass

# Schema for response body
class Employee(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt