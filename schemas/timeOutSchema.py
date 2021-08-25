from datetime import datetime, time
from pydantic import BaseModel

class TimeOutBase(BaseModel):
    employee_id: str
    time_log: str

# Schema for request body
class CreateTimeOut(TimeOutBase):
    pass

# Schema for response body
class TimeOut(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime