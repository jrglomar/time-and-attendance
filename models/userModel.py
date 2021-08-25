from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    user_type_id = Column(Integer, ForeignKey('user_types.id'), nullable=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    active_status = Column(String(255), server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    user_types = relationship('UserType', back_populates='users', lazy='joined')
    employees = relationship('Employee', back_populates='users')
