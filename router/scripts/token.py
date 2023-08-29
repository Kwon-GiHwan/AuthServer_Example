from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import APIRouter, Depends, HTTPException, status
import db.orm_connector as db
import crud.user as crud
#from api.fastapi import SECRET_KEY
import secrets

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
def user_token(token: str = Depends(oauth2_scheme),
               db: Session = Depends(db.get_db)):

    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

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

