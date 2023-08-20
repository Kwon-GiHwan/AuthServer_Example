#define crud for each user

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class User(Base):
    __tablename__ = 'item'

    id: Column(Integer, primary_key=True, index=True)
    category: Column(String, unique=True, index=True, nullable=False)
    price: Column(Integer, nullable=False)
    cost: Column(Integer, nullable=False)
    name: Column(String, index=True, nullable=False)
    description: Column(String, index=True, nullable=False)
    barcode: Column(String, index=True, nullable=False)
    duedate: Column(Datetime, index=True, nullable=False)
    size: Column(String, index=True, nullable=False)#small or large


    user = relationship("Item", back_populates="owner")#forein 키 추가
