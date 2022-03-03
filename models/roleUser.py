# Import Packages
from database import Base
from sqlalchemy import text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float, Text, Boolean, Date, Time
from sqlalchemy.orm import relationship


# same as user type model
class Role(Base):
    __tablename__ = 'roles'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    subsystem = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    redirect_url = Column(String(255), nullable=False)
    active_status = Column(String(255), nullable=True, server_default=text("'Active'"))
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_onupdate=text('NOW()'))

    users = relationship('UserRole', back_populates='role')