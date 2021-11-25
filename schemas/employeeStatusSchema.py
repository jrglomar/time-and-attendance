from datetime import datetime as dt
from pydantic import BaseModel

class EmployeeStatusBase(BaseModel):
    title: str

# Schema for request body
class CreateEmployeeStatus(EmployeeStatusBase):
    pass

# Schema for response body
class EmployeeStatus(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt

    