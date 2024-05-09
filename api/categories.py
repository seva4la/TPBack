from typing import List

from fastapi import APIRouter, Query, HTTPException

from servises.categories import categories_service

from schemas.categories import Categories, CategoriesCreate, TaskCreate, Task, CategoriesPost, TaskPost

router = APIRouter()


@router.post("/categories/creates", response_model=CategoriesCreate)
def categories_create(data: CategoriesCreate):
    user = categories_service.get_user_by_id(data.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return categories_service.categories_create(data)


@router.get("/categories/get", response_model=List[Categories])
def categories_get():
    return categories_service.categories_get()


@router.post("/categories/post_with_id", response_model=List[Categories])
def categories_get_with_id(data: CategoriesPost):
    user = categories_service.get_user_by_id(data.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return categories_service.categories_get_with_id(user)


@router.post("/tasks/post_with_id", response_model=List[Task])
def tasks_get_with_id(data: TaskPost):
    user = categories_service.get_user_by_id(data.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return categories_service.task_get_with_id(user)


@router.post("/tasks/create", response_model=Task)
def create_task(task: TaskCreate):
    category = categories_service.get_category_by_id(task.category_id)
    user = categories_service.get_user_by_id(task.user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return categories_service.task_create(task)
