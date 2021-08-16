from datetime import datetime as dt
from pydantic import BaseModel

class ShiftTypeBase(BaseModel):
    title: str

# Schema for request body
class CreateShiftType(ShiftTypeBase):
    pass

# Schema for response body
class ShiftType(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt