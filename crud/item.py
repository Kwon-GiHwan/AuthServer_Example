from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from datetime import datetime

from db.models import UserModel, ItemModel
import schemas.item as schema


def get_list(db: Session, user_id: int, cursor: int = 0, size: int = 10):

    total = 0#전체 갯수 조회하기
    item_list = db.query(schema.Item).filter(
        schema.Item.user_id == user_id, schema.Item.id > cursor).limit(size).all()

    return item_list  # (전체 건수, 페이징 적용된 질문 목록)

def get_item(db: Session, item_id: int):
    item = db.query(schema.Item).filter(schema.Item.id == item_id).first()

    return item  # (전체 건수, 페이징 적용된 질문 목록)

def search_initial(db: Session, user_id:int, cursor: int, item_initial: str, limit: int = 10):
    item_initial = item_initial.replace(' ', '')
    item_list = db.query(func.REPLACE(schema.Item.item_initial, ' ', '')).filter(
        schema.Item.user_id == user_id, schema.Item.id > cursor,
        schema.Item.item_initial.like("%" + item_initial + "%")
    ).limit(limit).all()

    return item_list

def search_name(db: Session, user_id:int, cursor: int, item_name: str, limit: int = 10):
    item_name = item_name.replace(' ', '')
    # item_list = db.query(func.REPLACE(models.Item.item_name, ' ', '')).filter(
    #     models.Item.user_id == user_id, models.Item.id > cursor,
    #     models.Item.item_name.like("%" + item_name + "%")
    # ).limit(limit).all()

    item_list = db.query(schema.Item).filter(
        schema.Item.user_id == user_id, schema.Item.id > cursor,
        func.regexp_replace(schema.Item.item_name, '\s+', '').like("%" + item_name + "%")
    ).limit(limit).all()

    return item_list


def create_item(db: Session, item: schema.ItemCreate, initial:str, user_id: int):

    db_item = ItemModel(**item.model_dump(), initial=initial, user_id=user_id)
    db.add(db_item)
    db.commit()
    # return db_item

def update_item(db: Session, item: schema.ItemUpdate):

    db.query(schema.Item).filter(schema.Item.id == item.id).update(**item.model_dump().pop('id'))
    db.commit()

def delete_item(db: Session, item: schema.Item):
    db.delete(item)
    db.commit()