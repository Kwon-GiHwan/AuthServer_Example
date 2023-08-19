from typing import Optional
from pydantic import BaseModel, validator
import re


# Shared properties
class UserBase(BaseModel):
    # email: Optional[EmailStr] = None
    # is_active: Optional[bool] = True

    is_superuser: bool = False
    full_name: Optional[str] = None




# Properties to receive via API on creation
class UserCreate(UserBase):
    phone: str
    password: str

    @validator('phone')
    def phone_validator(self, value):
        pattern = r"\d{3}-\d{4}-\d{4}$"
        match = re.match(pattern, value)
        if not match:
            raise ValueError('Invalid phone number: %s' % value)
        return value



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