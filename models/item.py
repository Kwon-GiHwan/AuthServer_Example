#define crud for each user

from sqlalchemy import Column, Integer, String, Datetime
from sqlalchemy.orm import relationship

from db.orm_connector import Base



class Item(Base):
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

    # question_id = Column(Integer, ForeignKey("question.id"))
    # question = relationship("Question", backref="answers")
    # user = relationship("Item", back_populates="owner")#forein 키 추가

class ItemCreate(Item):
    id: Column(Integer, primary_key=True, index=True)

