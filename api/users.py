from fastapi import APIRouter, Query

from servises.users import user_service

from schemas.users import User, UserUpdate, Reg

router = APIRouter()


@router.post("/user/register_user", response_model=UserUpdate)
def user_register_user(data: Reg):
    return user_service.register_user(data)


@router.post("/user/authentication_user", response_model=UserUpdate)
def user_authentication_user(username: str = Query(...), password: str = Query(...)):
    return user_service.authentication_user(username, password)
