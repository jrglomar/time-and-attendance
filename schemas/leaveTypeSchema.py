from datetime import datetime as dt
from pydantic import BaseModel

class LeaveTypeBase(BaseModel):
    title: str    

# Schema for request body
class CreateLeaveType(LeaveTypeBase):
    pass

# Schema for response body
class LeaveType(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt