from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.item import ItemList, ItemDelete, ItemCreate, ItemUpdate
import crud.item as crud
from db.models import UserModel
import db.orm_connector as db

from user import get_current_user

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/list", response_model=ItemList)
def read_item(db: Session = Depends(db.get_db),
                  page: int = 0, size: int = 10):

    total, _item_list = crud.get_item_list(
        db, skip=page*size, limit=size)
    return {
        'total': total,
        'item_list': _item_list
    }

@router.post("/create/", status_code=status.HTTP_204_NO_CONTENT)
def create_item(_item_create: ItemCreate,
                    db: Session = Depends(db.get_db)):

    crud.item.create_item(db=db, item_create=_item_create)

@router.post("/update/", status_code=status.HTTP_204_NO_CONTENT)
def update_item(_item_update: ItemUpdate,
                    db: Session = Depends(db.get_db),
                    current_user: UserModel = Depends(get_current_user)):

    db_item = crud.get_item(db, item_id=_item_update.item_id)

    if not db_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_item.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    crud.update_item(db=db, db_item=db_item,
                                  item_update=_item_update)
@router.post("/delete/", status_code=status.HTTP_204_NO_CONTENT)
def item_delete(_item_delete: ItemDelete,
                    db: Session = Depends(db.get_db),
                    current_user: UserModel = Depends(get_current_user)):

    db_item = crud.get_item(db, item_id=_item_delete.item_id)

    if not db_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_item.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    crud.delete_item(db=db, db_item=db_item)

