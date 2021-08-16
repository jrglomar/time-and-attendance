from datetime import datetime as dt
from pydantic import BaseModel

class TimeOutBase(BaseModel):
    employee_id: int

# Schema for request body
class CreateTimeOut(TimeOutBase):
    pass

# Schema for response body
class TimeOut(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt