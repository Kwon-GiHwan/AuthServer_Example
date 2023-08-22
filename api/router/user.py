#CRUD
from fastapi import APIRouter, Depends, HTTPException, status
from starlette.middleware.cors import CORSMiddleware
# from ..dependencies import get_token_header
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import timedelta, datetime


import crud.user as crud
import schemas.user as schema
import db.orm_connector as db

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
import secrets
secrets.token_hex(32)
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(db.get_db)],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/register/",
    tags=["users"],
    responses={403: {"description": "Operation forbidden"}},
    status_code=status.HTTP_204_NO_CONTENT,
)
async def register(_user_create: schema.UserCreate, db: Session = Depends(db.get_db)):
    user = crud.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    crud.create_user(db=db, user_create=_user_create)


@router.post(
    "/login/",
    tags=["users"],
    status_code=200,
    # responses={403: {"description": "Operation forbidden"}},
    response_model=schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(db.get_db)):

    # check user and password
    user = crud.get_user(db, form_data.username)
    if not user or not crud.pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # make access token
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }

def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(db.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    else:
        user = crud.get_user(db, username=username)
        if user is None:
            raise credentials_exception
        return user