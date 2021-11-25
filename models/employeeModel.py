from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from database import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    employee_type_id = Column(Integer, ForeignKey('employee_types.id'), nullable=True)
    employee_status_id = Column(Integer, ForeignKey('employee_status.id'), nullable=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=True)
    shift_type_id = Column(Integer, ForeignKey('shift_types.id'), nullable=True)
    attendance_status = Column(String(255), nullable=True)
    monday = Column(String(255), nullable=True)
    tuesday = Column(String(255), nullable=True)
    wednesday = Column(String(255), nullable=True)
    thursday = Column(String(255), nullable=True)
    friday = Column(String(255), nullable=True)
    saturday = Column(String(255), nullable=True)
    sunday = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    users = relationship('User', back_populates='employees', lazy='joined')
    employee_types = relationship('EmployeeType', back_populates='employees', lazy='joined')
    employee_status = relationship('EmployeeStatus', back_populates='employees', lazy='joined')
    shift_types = relationship('ShiftType', back_populates='employees', lazy='joined')
    time_ins = relationship('TimeIn', back_populates='employees')
    time_outs = relationship('TimeOut', back_populates='employees')
    attendances = relationship('Attendance', back_populates='employees')
    leaves = relationship('Leave', back_populates='employees')
    missed_times = relationship('MissedTime', back_populates='employees')
    shift_changes = relationship('ShiftChange', back_populates='employees')
