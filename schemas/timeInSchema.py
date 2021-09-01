from datetime import datetime, time, date
from pydantic import BaseModel

class TimeInBase(BaseModel):
    employee_id: str
    time_log: str

# Schema for request body
class CreateTimeIn(TimeInBase):
    pass

# Schema for request body
class CreateCustomTimeIn(BaseModel):
    employee_id: str
    time_log: str
    created_at: date

class GetTimeIn(BaseModel):
    date_today: date

# Schema for response body
class TimeIn(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime