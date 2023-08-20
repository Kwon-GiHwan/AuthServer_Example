import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer

SizeType = Annotated[
    str,
    StringConstraints(to_upper=True, pattern=r'(?:small|large)'),
]

class Item(BaseModel):
    id: int
    category: str
    price: str
    src_price: str
    name: str
    description: str
    barcode: str
    duedate: datetime
    size: SizeType#small or large

    @validator('category', 'price')
    def check_null(self, value, values):
        for k, v in values.items():
            if not v :
                raise ValueError('Invalid value')#완성해야됨
        if not value or not value.strip():
            raise ValueError('Empty string')
        return value

class ItemList(BaseModel):
    total: int = 0
    question_list: list[Item] = []