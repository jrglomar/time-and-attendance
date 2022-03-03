# Import Packages
from database import Base
from sqlalchemy import text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float, Text, Boolean, Date, Time
from sqlalchemy.orm import relationship

#same as userModel

class InternalUser(Base):
    __tablename__ = 'internal_users'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    roles = relationship('UserRole', back_populates='user')