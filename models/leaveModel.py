from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Leave(Base):
    __tablename__ = 'leaves'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    leave_type_id = Column(Integer, ForeignKey('leave_types.id'), nullable=False)
    title = Column(String(255), nullable=False)
    reason = Column(String(500), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    leave_types = relationship('LeaveType', back_populates='leaves', lazy='joined')
    employees = relationship('Employee', back_populates='leaves', lazy='joined')
