import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime 
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

#User Table
class User(Base):
    __tablename__ = 'users' 
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    name = Column(String(50))
    password = Column(String(64))
    group = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f'{self.id}|{self.name}|{self.group}'
