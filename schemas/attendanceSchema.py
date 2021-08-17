from datetime import datetime as dt
from pydantic import BaseModel

class AttendanceBase(BaseModel):
    employee_id: str
    shift_type_id: str
    time_in_id: str
    time_out_id: str
    hours_worked: str

# Schema for request body
class CreateAttendance(AttendanceBase):
    pass

# Schema for response body
class Attendance(BaseModel):
    # active_status: str
    created_at: dt
    updated_at: dt