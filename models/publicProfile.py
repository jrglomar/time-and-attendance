# Import Packages
from database import Base
from sqlalchemy import text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float, Text, Boolean, Date, Time
from sqlalchemy.orm import relationship


class PublicProfile(Base):
    __tablename__ = 'public_profiles'

    id = Column(String(36), primary_key=True, nullable=False, default=text('UUID()'))
    user_id = Column(String(36), ForeignKey('public_users.id'), nullable=True)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    suffix_name = Column(String(255), nullable=True)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(255), nullable=False)
    house_street = Column(String(255), nullable=False)
    barangay = Column(String(255), nullable=False)
    municipality = Column(String(255), nullable=False)
    province = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    contact_number = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    full_address = Column(String(255), nullable=False)

    public_user = relationship('PublicUser', back_populates='profile')