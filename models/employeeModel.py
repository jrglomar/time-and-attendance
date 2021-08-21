from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from database import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    employee_type_id = Column(Integer, ForeignKey('employee_types.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    shift_type_id = Column(Integer, ForeignKey('shift_types.id'), nullable=True)
    monday = Column(Boolean, nullable=True)
    tuesday = Column(Boolean, nullable=True)
    wednesday = Column(Boolean, nullable=True)
    thursday = Column(Boolean, nullable=True)
    friday = Column(Boolean, nullable=True)
    saturday = Column(Boolean, nullable=True)
    sunday = Column(Boolean, nullable=True)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    users = relationship('User', back_populates='employees', lazy='joined')
    employee_types = relationship('EmployeeType', back_populates='employees', lazy='joined')
    shift_types = relationship('ShiftType', back_populates='employees', lazy='joined')
    time_ins = relationship('TimeIn', back_populates='employees', lazy='joined')
    time_outs = relationship('TimeOut', back_populates='employees', lazy='joined')
    attendances = relationship('Attendance', back_populates='employees', lazy='joined')
    leaves = relationship('Leave', back_populates='employees', lazy='joined')
