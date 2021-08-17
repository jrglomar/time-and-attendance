from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class LeaveType(Base):
    __tablename__ = 'leave_types'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    title = Column(String(255), nullable=False)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    leaves = relationship('Leave', back_populates='leave_types')
    
