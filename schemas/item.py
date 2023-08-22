import datetime
from typing_extensions import Annotated
from pydantic import BaseModel, validator, constr

SizeType = Annotated[
    str,
    constr(to_lower=True, pattern=r'(?:small|large)'),
]

class Item(BaseModel):
    item_id: int
    category: str
    price: str
    src_price: str
    name: str
    initial: str#initial of item
    description: str
    barcode: str
    duedate: datetime
    size: SizeType#small or large

    @validator('*')#수정하기
    def check_null(self, value):
        if not isinstance(value, str):
            raise ValueError('Empty string {}', value )#고치기
        return value

    class Config:
        orm_mode = True

class ItemList(BaseModel):
    total: int = 0
    item_list: list[Item] = []

class ItemCreate(BaseModel):
    pass
class ItemUpdate(Item):
    item_id: int

class ItemDelete(BaseModel):
    item_id: int
