from datetime import datetime as dt
from pydantic import BaseModel

class TimeInBase(BaseModel):
    employee_id: str

# Schema for request body
class CreateTimeIn(TimeInBase):
    pass

# Schema for response body
class TimeIn(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt