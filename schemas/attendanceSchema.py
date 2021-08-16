from datetime import datetime as dt
from pydantic import BaseModel

class AttendanceBase(BaseModel):
    employee_id: int
    shift_type_id: int
    time_in_id: int
    time_out_id: int
    hours_worked: int

# Schema for request body
class CreateAttendance(AttendanceBase):
    pass

# Schema for response body
class Attendance(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt