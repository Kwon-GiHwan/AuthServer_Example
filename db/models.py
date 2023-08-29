#define crud for each user

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from db.orm_connector import Base

class ItemModel(Base):
    __tablename__ = "item"

    id : Mapped[int] =  mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] =  mapped_column(Integer, nullable=False)
    cost: Mapped[int] =  mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    initial: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    barcode: Mapped[str] = mapped_column(String, nullable=False)
    duedate: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    size: Mapped[str] = mapped_column(String, nullable=False)#small or large
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)#수정하기

class UserModel(Base):
    __tablename__ = 'user'

    id : Mapped[int] =  mapped_column(Integer, primary_key=True)
    phone : Mapped[str] = mapped_column(String, nullable=False)
    password : Mapped[str] = mapped_column(String, nullable=False)
