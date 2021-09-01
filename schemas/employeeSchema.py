from datetime import datetime as dt
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean

class EmployeeBase(BaseModel):
    user_id: str
    shift_type_id: str
    employee_type_id: str
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