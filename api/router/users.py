#CRUD
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.post(
    "/",
    tags=["users"],
    responses={403: {"description": "Operation forbidden"}},
)
async def register(user_id: str, user_pw):
    #check if id is in db already
    #return error or check response


    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}

@router.post(
    "/login/",
    tags=["users"],
    status_code=200,
    responses={403: {"description": "Operation forbidden"}},
)
async def login(user_info: models.UserRegister):
    is_exist = await is_email_exist(user_info.email)

    if not user_info.email or not user_info.pw:
        return JSONResponse(status_code=400, content=dict(msg="Email and PW must be provided'"))
    if not is_exist:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))

    user = Users.get(email=user_info.email)
    is_verified = bcrypt.checkpw(user_info.pw.encode("utf-8"), user.pw.encode("utf-8"))

    if not is_verified:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))
    token = dict(
        Authorization=f"Bearer {create_access_token(data=UserToken.from_orm(user).dict(exclude={'pw', 'marketing_agree'}),)}")
    return token
@router.post(
    "/",
    tags=["users"],
    responses={403: {"description": "Operation forbidden"}},
)
async def logout(user_id: str, user_pw):
    #token related operations

    return {"item_id": item_id, "name": "The great Plumbus"}
