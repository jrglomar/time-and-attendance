from datetime import datetime, time, date
from pydantic import BaseModel

class TimeOutBase(BaseModel):
    employee_id: str
    time_log: str

# Schema for request body
class CreateTimeOut(TimeOutBase):
    pass

class CreateCustomTimeOut(BaseModel):
    employee_id: str
    time_log: str
    created_at: date

class GetTimeOut(BaseModel):
    date_today: date

# Schema for response body
class TimeOut(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime