# Import Packages
from database import Base
from sqlalchemy import text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float, Text, Boolean, Date, Time
from sqlalchemy.orm import relationship


#** PUBLIC USER
class PublicUser(Base):
    __tablename__ = 'public_users'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
    is_blacklist = Column(Boolean, default=text('0'))

    profile = relationship('PublicProfile', back_populates='public_user', uselist=False)