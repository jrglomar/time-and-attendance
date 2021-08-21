from datetime import datetime as dt
from pydantic import BaseModel

class EmployeeTypeBase(BaseModel):
    title: str

# Schema for request body
class CreateEmployeeType(EmployeeTypeBase):
    pass

# Schema for response body
class EmployeeType(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt