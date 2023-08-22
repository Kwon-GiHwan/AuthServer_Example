#define crud for each user

from sqlalchemy import Column, Integer, String, Datetime, ForeignKey
from sqlalchemy.orm import relationship

from .orm_connector import Base

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    user = relationship("Item", back_populates="user")


class ItemModel(Base):
    __tablename__ = 'item'

    id: Column(Integer, primary_key=True, index=True)
    category: Column(String, unique=True, index=True, nullable=False)
    price: Column(Integer, nullable=False)
    cost: Column(Integer, nullable=False)
    name: Column(String, index=True, nullable=False)
    initial: Column(String, index=True, nullable=False)
    description: Column(String, index=True, nullable=False)
    barcode: Column(String, index=True, nullable=False)
    duedate: Column(Datetime, index=True, nullable=False)
    size: Column(String, index=True, nullable=False)#small or large
    #index True 고려하기
    user_id = Column(Integer, ForeignKey("user.id"))#수정하기
    # question = relationship("Question", backref="answers")
    # user = relationship("Item", back_populates="owner")#forein 키 추가


