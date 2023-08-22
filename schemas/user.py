from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, validator, StringConstraints
import re

PhoneNumber = Annotated[
    str,
    StringConstraints(pattern=r"\d{3}-\d{4}-\d{4}$"),
]

class User(BaseModel):
    id: int
    phone: PhoneNumber
    password: str

    class Config:
        orm_mode = True

# Properties to receive via API on creation
# class UserCreate(UserBase):
class UserCreate(BaseModel):
    # id: int
    # phone: str
    phone: PhoneNumber
    password: str

    @validator('phone', 'password')
    def check_null(self, value):
        if not value or not value.strip():
            raise ValueError('Empty string')
        return value

    # @validator('phone')
    # def phone_validate(self, value):
    #     pattern = r"\d{3}-\d{4}-\d{4}$"
    #     match = re.match(pattern, value)
    #     if not match:
    #         raise ValueError('Invalid phone number: %s' % value)
    #     return value
class Token(BaseModel):
    access_token: str
    token_type: str
    username: str