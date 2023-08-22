from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, validator, StringConstraints
import re

PhoneNumber = Annotated[
    str,
    StringConstraints(pattern=r"\d{3}-\d{4}-\d{4}$"),
]


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


#Item수ㅅ정에 사용 가능 override 사용할것
# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    username: str