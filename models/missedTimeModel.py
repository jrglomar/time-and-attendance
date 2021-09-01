from sqlalchemy import Integer, String, DateTime, text, Time
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class MissedTime(Base):
    __tablename__ = 'missed_times'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    approved_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    time_log = Column(Time, nullable=False)
    time_log_type = Column(String(255), nullable=False)
    proof = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False, server_default=text("'Pending'"))
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    employees = relationship('Employee', back_populates='missed_times', lazy='joined')
    users = relationship('User', back_populates='missed_times', lazy='joined')
