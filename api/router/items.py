from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),
                  page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size)
    return {
        'total': total,
        'question_list': _question_list
    }

@router.post("/create/", status_code=status.HTTP_204_NO_CONTENT)
def create_item(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)

@router.post("/update/", status_code=status.HTTP_204_NO_CONTENT)
def update_item(_question_create: question_schema.QuestionCreate,
                db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)

@router.post("/delete/", status_code=status.HTTP_204_NO_CONTENT)
def update_item(_question_create: question_schema.QuestionCreate,
                db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)

