from typing import List

from pydantic import BaseModel

class CategoriesCreate(BaseModel):
    title: str

class Categories(BaseModel):
    id: str
    title: str
    tasks: int

    class Config:
        orm_mode =True