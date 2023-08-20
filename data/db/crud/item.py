from sqlalchemy.orm import Session

from . import models, schemas

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
def get_items(db: Session, skip: int = 0, limit: int = 10):

    total = 0
    item_list = db.query(models.Item).filter(Item.userid == User.id, Item.id > page).limit(limit).all()

    return total, item_list  # (전체 건수, 페이징 적용된 질문 목록)

#get user id -> filter where user_id == getuser_id and id>cursor, limit=10

def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item