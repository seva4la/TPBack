from typing import List

import pydantic
from schemas.categories import Categories, Task

class User(pydantic.BaseModel):
    id: str
    username: str
    password: str


class UserUpdate(pydantic.BaseModel):
    username: str
    id: str


class Reg(pydantic.BaseModel):
    username: str
    password: str
    password1: str
