from datetime import datetime, time, date
from pydantic import BaseModel
from typing import List, Optional

class MissedTimeBase(BaseModel):
    date: date
    time_log: str
    time_log_type: str
    employee_id: str
    proof: Optional[str] = None

# Schema for request body
class CreateMissedTime(MissedTimeBase):
    pass

class UpdateMissedTime(BaseModel):
    status: str

# Schema for response body
class MissedTime(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime