from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional

class LeaveBase(BaseModel):
    employee_id: str
    leave_type_id: str
    leave_sub_type_id: str
    title: str
    reason: str
    start_date: date
    end_date: date
    status: Optional[str]
    
# Schema for request body
class CreateLeave(LeaveBase):
    pass

class GetLeave(BaseModel):
    start_date: date
    
class GetLeaveReport(BaseModel):
    start_date: date
    end_date: date
    
# Schema for response body
class Leave(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime