from typing import List
from typing import Optional
from pydantic import BaseModel, Field

class Task(BaseModel):
    id: str
    title: str
    description: str
    category_id: str
    user_id: str

    class Config:
        orm_mode = True


class CategoriesCreate(BaseModel):
    title: str
    user_id: str


class Categories(BaseModel):
    id: str
    title: str
    tasks: List[Task]
    user_id: str

    class Config:
        orm_mode = True


class CategoriesPost(BaseModel):
    user_id: str


class TaskPost(BaseModel):
    user_id: str


class TaskCreate(BaseModel):
    title: str
    description: str
    category_id: str
    user_id: str
