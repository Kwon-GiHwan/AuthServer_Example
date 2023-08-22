
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models import UserModel


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user_create: UserCreate):
    db_user = UserModel(username=user_create.phone,
                   password=pwd_context.hash(user_create.password))
    db.add(db_user)
    db.commit()

def get_user(db: Session, user_create: UserCreate):
    return db.query(UserModel).filter(
        (UserModel.phone == user_create.phone)
    ).first()
