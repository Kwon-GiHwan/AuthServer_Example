from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from schemas.item import ItemList, ItemDelete, ItemCreate, ItemUpdate
from schemas.response import response_builder
import crud.item as crud
from db.models import UserModel
import db.orm_connector as db

from ..auth.token import user_token
from ..scripts.word_frag import separate

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/list", response_model=ItemList)
async def read_item(db: Session = Depends(db.get_db),
                current_user: UserModel = Depends(user_token),
                cursor: int = 0, size: int = 10):

    item_list = crud.get_list(
        db, user_id=current_user.user_id, cursor=cursor, size=size)


    return JSONResponse(status_code=status.HTTP_200_OK, content=response_builder(200, 'ok', item_list))

@router.post("/create/", status_code=status.HTTP_204_NO_CONTENT)
async def create_item(item: ItemCreate,
                db: Session = Depends(db.get_db),
                current_user: UserModel = Depends(user_token)):

    name_initial = separate(item.name)
    crud.create_item(db=db, item=item, initial=name_initial, user_id=current_user.user_id)

@router.post("/update/", status_code=status.HTTP_204_NO_CONTENT)
async def update_item(item: ItemUpdate,
                db: Session = Depends(db.get_db),
                current_user: UserModel = Depends(user_token)):

    db_item = crud.get_item(db, item_id=item.item_id)

    if not db_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=response_builder(400, '데이터 오류'))

    if current_user.id != db_item.user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=response_builder(400, '권한 오류'))
    crud.update_item(db=db,item=item)
@router.post("/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item: ItemDelete,
                db: Session = Depends(db.get_db),
                current_user: UserModel = Depends(user_token)):

    db_item = crud.get_item(db, item_id=item.item_id)

    if not db_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=response_builder(400, '데이터 오류'))
    if current_user.id != db_item.user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=response_builder(400, '권한 오류'))
    crud.delete_item(db=db, item=item)

