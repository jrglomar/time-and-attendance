from sqlalchemy import Integer, String, DateTime, text, Time
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Attendance(Base):
    __tablename__ = 'attendances'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    time_in_id = Column(Integer, ForeignKey('time_ins.id'), nullable=False)
    time_out_id = Column(Integer, ForeignKey('time_outs.id'), nullable=False)
    hours_worked = Column(Integer, nullable=False)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    employees = relationship('Employee', back_populates='attendances', lazy='joined')
    time_ins = relationship('TimeIn', back_populates='attendances', lazy='joined')
    time_outs = relationship('TimeOut', back_populates='attendances', lazy='joined')
    
