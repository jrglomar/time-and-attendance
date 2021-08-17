from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    first_name = Column(String(255), nullable=True)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    suffix_name = Column(String(255), nullable=True)
    full_name = Column(String(255), nullable=True)
    birth_date = Column(DateTime, nullable=True)
    gender = Column(String(255), nullable=True)
    house_number = Column(String(255), nullable=True)
    street = Column(String(255), nullable=True)
    barangay = Column(String(255), nullable=True)
    municipality = Column(String(255), nullable=True)
    province = Column(String(255), nullable=True)
    picture = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    users = relationship('User', back_populates='user_profiles')
    employees = relationship('Employee', back_populates='user_profiles')
