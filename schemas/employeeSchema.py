from datetime import datetime as dt
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean
from typing import List, Optional

class EmployeeBase(BaseModel):
    user_id: Optional[str]
    shift_type_id: Optional[str]
    employee_type_id: Optional[str]
    employee_status_id: Optional[str]
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    saturday: str
    sunday: str

# Schema for request body
class CreateEmployee(EmployeeBase):
    pass

class UpdateTimeLog(BaseModel):
    time_status: str

# Schema for response body
class Employee(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt