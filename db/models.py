#define crud for each user

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .orm_connector import Base

class ItemModel(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    category: Column(String, nullable=False)
    price: Column(Integer, nullable=False)
    cost: Column(Integer, nullable=False)
    name: Column(String, nullable=False)
    initial: Column(String, nullable=False)
    description: Column(String, nullable=False)
    barcode: Column(String, nullable=False)
    duedate: Column(DateTime, nullable=False)
    size: Column(String, nullable=False)#small or large
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)#수정하기

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)






