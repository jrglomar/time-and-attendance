from datetime import datetime, date
from pydantic import BaseModel

class AttendanceBase(BaseModel):
    employee_id: str
    time_in_id: str

# Schema for request body
class CreateAttendance(AttendanceBase):
    pass

class GetAttendance(BaseModel):
    start_date: datetime
    end_date: datetime

class GetAttendanceOne(BaseModel):
    start_date: datetime
    end_date: datetime
    employee_id: str

class UpdateAttendanceOut(BaseModel):
    time_out_id: str

class GetAttendanceReport(BaseModel):
    start_date: date
    end_date: date
    

# Schema for response body
class Attendance(BaseModel):
    # active_status: str
    created_at: datetime
    updated_at: datetime