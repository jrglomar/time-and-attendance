from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class EmployeeType(Base):
    __tablename__ = 'employee_types'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    title = Column(String(255), nullable=False)
    active_status = Column(String(255), nullable=True, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    employees = relationship('Employee', back_populates='employee_types', lazy='joined')
    
