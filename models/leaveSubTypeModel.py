from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class LeaveSubType(Base):
    __tablename__ = 'leave_sub_types'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    title = Column(String(255), nullable=False)
    number_of_days = Column(String(255), nullable=False)
    leave_type_id = Column(String(36), ForeignKey('leave_types.id'), nullable=False)
    active_status = Column(String(255), nullable=False, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    leave_types = relationship('LeaveType', back_populates='leave_sub_types', lazy='joined')
    leaves = relationship('Leave', back_populates='leave_sub_types')
