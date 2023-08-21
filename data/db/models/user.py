#define crud for each user

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..orm_connector import Base




class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    items = relationship("Item", back_populates="owner")#relation 고치기
