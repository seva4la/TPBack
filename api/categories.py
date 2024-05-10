from typing import List

from fastapi import APIRouter, Query, HTTPException

from servises.categories import categories_service

from schemas.categories import Categories, CategoriesCreate, TaskCreate, Task, CategoriesPost, TaskPost

from typing import Optional

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


from fastapi import Path


@router.delete("/tasks/delete/{task_id}")
def delete_task(task_id: str = Path(..., title="The ID of the task to delete")):
    deleted_task = categories_service.delete_task_by_id(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@router.delete("/categories/delete/{category_id}")
def delete_category(category_id: str):
    deleted_category = categories_service.delete_category_and_tasks(category_id)
    if deleted_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category and associated tasks deleted successfully"}


@router.put("/categories/{category_id}")
def update_category(
        category_id: str,
        title: Optional[str] = None,
):
    updated_category = categories_service.update_category(
        category_id, title)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category updated successfully"}


@router.put("/tasks/{task_id}")
def update_task(
        task_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None
):
    updated_task = categories_service.update_task(
        task_id, title, description)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task updated successfully"}
