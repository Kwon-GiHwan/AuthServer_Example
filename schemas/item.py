import datetime
from typing_extensions import Annotated
from pydantic import BaseModel, validator, constr

SizeType = constr(to_lower=True, pattern=r'(?:small|large)')

class Item(BaseModel):
    id: int
    category: str
    price: str
    src_price: str
    name: str
    initial: str#initial of item
    description: str
    barcode: str
    duedate: datetime.datetime
    size: SizeType#small or large
    user_id: int

    @validator('*')#수정하기
    def check_null(cls, value):
        if not isinstance(value, str):
            raise ValueError('Empty string {}', value )#고치기
        return value

    class Config:
        from_attributes = True

class ItemList(BaseModel):
    total: int = 0
    item_list: list[Item] = []

class ItemCreate(BaseModel):
    category: str
    price: str
    src_price: str
    name: str
    description: str
    barcode: str
    duedate: datetime.datetime
    size: SizeType
class ItemUpdate(Item):
    category: str
    price: str
    src_price: str
    name: str
    description: str
    barcode: str
    duedate: datetime.datetime
    size: SizeType


class ItemDelete(BaseModel):
    id: int
