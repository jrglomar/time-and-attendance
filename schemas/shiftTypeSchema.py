from datetime import datetime, time
from pydantic import BaseModel

class ShiftTypeBase(BaseModel):
    title: str
    start_time: time
    end_time: time

# Schema for request body
class CreateShiftType(ShiftTypeBase):
    pass

# Schema for response body
class ShiftType(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime