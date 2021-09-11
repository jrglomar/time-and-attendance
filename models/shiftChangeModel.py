from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from database import Base

class ShiftChange(Base):
    __tablename__ = 'shift_changes'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    employee_id = Column(String(36), ForeignKey('employees.id'), nullable=True)
    employee_type_id = Column(String(36), nullable=True)
    user_id = Column(String(36), nullable=True)
    shift_type_id = Column(String(36), ForeignKey('shift_types.id'), nullable=True)
    monday = Column(String(255), nullable=True)
    tuesday = Column(String(255), nullable=True)
    wednesday = Column(String(255), nullable=True)
    thursday = Column(String(255), nullable=True)
    friday = Column(String(255), nullable=True)
    saturday = Column(String(255), nullable=True)
    sunday = Column(String(255), nullable=True)
    status = Column(String(255), nullable=False, server_default=text("'Pending'"))
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))


    employees = relationship('Employee', back_populates='shift_changes', lazy='joined')
    shift_types = relationship('ShiftType', back_populates='shift_changes', lazy='joined')
    