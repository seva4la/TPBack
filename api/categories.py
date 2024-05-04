from typing import List

from fastapi import APIRouter, Query

from servises.categories import categories_service

from schemas.categories import Categories, CategoriesCreate


router = APIRouter()


@router.post("/categories/creates", response_model=CategoriesCreate)
def categories_create(data: CategoriesCreate):
    return categories_service.categories_create(data)

@router.get("/categories/get", response_model=List[Categories])
def categories_get():
    return categories_service.categories_get()