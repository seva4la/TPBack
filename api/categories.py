from typing import List

from fastapi import APIRouter, Query, HTTPException

from servises.categories import categories_service

from schemas.categories import Categories, CategoriesCreate, TaskCreate, Task

router = APIRouter()


@router.post("/categories/creates", response_model=CategoriesCreate)
def categories_create(data: CategoriesCreate):
    return categories_service.categories_create(data)


@router.get("/categories/get", response_model=List[Categories])
def categories_get():
    return categories_service.categories_get()


@router.post("/tasks/create", response_model=Task)
def create_task(task: TaskCreate):
    category = categories_service.get_category_by_id(task.category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return categories_service.task_create(task)


@router.get("/tasks", response_model=List[Task])
def get_tasks():
    return categories_service.get_tasks()
