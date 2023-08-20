#define crud for each user

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    # full_name = Column(String, index=True)
    phone = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    # is_active = Column(Boolean(), default=True)
    # is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")#relation 고치기
