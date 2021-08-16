from sqlalchemy import Integer, String, DateTime, text, Time
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ShiftType(Base):
    __tablename__ = 'shift_types'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    employees = relationship('Employee', back_populates='shift_types')
    attendances = relationship('Attendance', back_populates='shift_types')