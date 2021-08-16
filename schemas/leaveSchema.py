from datetime import datetime as dt
from pydantic import BaseModel

class LeaveBase(BaseModel):
    employee_id: int
    leave_type_id: int
    title: str
    reason: str
    start_date: dt
    end_date: dt
    
# Schema for request body
class CreateLeave(LeaveBase):
    pass

# Schema for response body
class Leave(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt