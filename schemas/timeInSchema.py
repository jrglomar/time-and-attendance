from datetime import datetime, time
from pydantic import BaseModel

class TimeInBase(BaseModel):
    employee_id: str
    time_log: str

# Schema for request body
class CreateTimeIn(TimeInBase):
    pass

# Schema for response body
class TimeIn(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime