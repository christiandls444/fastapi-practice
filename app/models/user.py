from sqlalchemy import Column, Integer, Boolean, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "userschema"}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=True)

    
    