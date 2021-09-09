from datetime import datetime, date
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean
from typing import List, Optional

class ShiftChangeBase(BaseModel):
    user_id: Optional[str]
    shift_type_id: Optional[str]
    employee_type_id: Optional[str]
    employee_id: Optional[str]
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    saturday: str
    sunday: str

# Schema for request body
class CreateShiftChange(ShiftChangeBase):
    pass

class UpdateShiftChange(BaseModel):
    status: str
    
class GetShiftChangeReport(BaseModel):
    start_date: date
    end_date: date

# Schema for response body
class ShiftChange(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime