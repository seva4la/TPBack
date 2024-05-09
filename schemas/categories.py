from typing import List
from typing import Optional
from pydantic import BaseModel, Field


class Task(BaseModel):
    id: str
    title: str
    description: str
    category_id: str

    class Config:
        orm_mode = True


class CategoriesCreate(BaseModel):
    title: str


class Categories(BaseModel):
    id: str
    title: str
    tasks: List[Task]

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    title: str
    description: str
    category_id: str
