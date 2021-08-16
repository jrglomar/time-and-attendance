from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    user_type_id = Column(Integer, ForeignKey('user_types.id'), nullable=False)
    user_profile_id = Column(Integer, ForeignKey('user_profiles.id'), nullable=False)
    shift_type_id = Column(Integer, ForeignKey('shift_types.id'), nullable=False)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    user_types = relationship('UserType', back_populates='employees')
    user_profiles = relationship('UserProfile', back_populates='employees')
    shift_types = relationship('ShiftType', back_populates='employees')
    time_ins = relationship('TimeIn', back_populates='employees')
    time_outs = relationship('TimeOut', back_populates='employees')
    attendances = relationship('Attendance', back_populates='employees')
    leaves = relationship('Leave', back_populates='employees')
