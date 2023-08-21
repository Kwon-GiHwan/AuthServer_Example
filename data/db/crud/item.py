from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from  import models, schemas
from ..models.item import ItemCreate


def get_list(db: Session, user_id: int, cursor: int = 0, limit: int = 10):

    total = 0#전체 갯수 조회하기
    item_list = db.query(models.Item).filter(
        models.Item.user_id == user_id, models.Item.id > cursor).limit(limit).all()

    return total, item_list  # (전체 건수, 페이징 적용된 질문 목록)

def get_detail(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.item_id == item_id).first()

    return item  # (전체 건수, 페이징 적용된 질문 목록)

def search_initial(db: Session, user_id:int, cursor: int, item_initial: str, limit: int = 10):
    item_initial = item_initial.replace(' ', '')
    item_list = db.query(func.REPLACE(models.Item.item_initial, ' ', '')).filter(
        models.Item.user_id == user_id, models.Item.id > cursor,
        models.Item.item_initial.like("%" + item_initial + "%")
    ).limit(limit).all()

    return item_list

def search_name(db: Session, user_id:int, cursor: int, item_name: str, limit: int = 10):
    item_name = item_name.replace(' ', '')
    # item_list = db.query(func.REPLACE(models.Item.item_name, ' ', '')).filter(
    #     models.Item.user_id == user_id, models.Item.id > cursor,
    #     models.Item.item_name.like("%" + item_name + "%")
    # ).limit(limit).all()

    item_list = db.query(models.Item).filter(
        models.Item.user_id == user_id, models.Item.id > cursor,
        func.regexp_replace(models.Item.item_name, '\s+', '').like("%" + item_name + "%")
    ).limit(limit).all()

    return item_list


def create_item(db: Session, item: ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now())
    db.add(db_question)
    db.commit()

def update_question(db: Session, db_question: Question,
                    question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()

def delete_question(db: Session, db_question: Question):
    db.delete(db_question)
    db.commit()