from fastapi import APIRouter
from schemas.schemas import User, UserCreate, UserRestore, Response, Credentials
from services.service import user_service

router = APIRouter()


@router.post("/users", response_model=User,
)
def register_user(data: UserCreate):
    return user_service.register_user(data)

@router.post('/login', response_model = User)
def auth(data: Credentials):
    return user_service.auth(data)

@router.get(
    "/users",
    status_code=200,
    response_model=list[User], )
def get_users():
    return user_service.get_users()


@router.put(
    "/user_update",
    response_model=User,
)
def update_user(
        payload: UserRestore):  # -> User:
    return user_service.update_user(payload)