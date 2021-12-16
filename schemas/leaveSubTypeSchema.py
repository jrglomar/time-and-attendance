from datetime import datetime, date
from pydantic import BaseModel

class LeaveSubTypeBase(BaseModel):
    title: str
    leave_type_id: str
    number_of_days: str
    
# Schema for request body
class CreateLeaveSubType(LeaveSubTypeBase):
    pass

# Schema for response body
class LeaveSubType(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime