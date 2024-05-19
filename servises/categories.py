from __future__ import annotations

import json
from typing import List


import sql.db_categories as db
import sql.db_users
import sql.db_users as db_us
from schemas.categories import CategoriesCreate, Categories, TaskCreate, Task
import uuid
from typing import Optional
from servises.users import User


class CategoriesService:

    def categories_create(self, data: CategoriesCreate) -> CategoriesCreate:
        categ = Categories(
            id=str(uuid.uuid4()), title=data.title, tasks=[], user_id=data.user_id)
        return db.createCategories(categ)

    def categories_get(self):
        return db.get_categories()

    def task_create(self, data: TaskCreate) -> Task:
        task = Task(
            id=str(uuid.uuid4()), title=data.title, description=data.description, category_id=data.category_id,
            user_id=data.user_id, color=data.color)
        return db.createTask(task)

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        user = sql.db_users.get_user_by_id(sql.db_users.session, user_id)
        if user:
            return User(id=user.id, password=user.password, username=user.username)
        return None

    def get_category_by_id(self, category_id: str) -> Optional[Categories]:
        category = db.get_category_by_id(db.session, category_id)
        if category:
            return Categories(id=category.id, title=category.title, tasks=[], user_id=category.user_id)
        return None
 
    def categories_get_with_id(self, UserWithId: User) -> Optional[User]:
        user = User(
            id=UserWithId.id, password=UserWithId.password, username=UserWithId.username)
        return db.get_categories_with_id(user)

    def task_get_with_id(self, UserWithId: User) -> Optional[User]:
        user = User(
            id=UserWithId.id, password=UserWithId.password, username=UserWithId.username)
        return db.get_task_with_id(user)

    def delete_task_by_id(self, task_id: str):
        task = sql.db_categories.get_task_from_db_by_id(task_id)
        if task:
            sql.db_categories.delete_task_by_id(task_id)
            return Task(**task.__dict__)
        return None

    def delete_category_and_tasks(self, category_id: str):
        category = self.get_category_by_id(category_id)
        if category is None:
            return None
        db.delete_category_and_tasks(category_id)
        return category

    def update_category(self, category_id: str, title: Optional[str] = None):
        category = self.get_category_by_id(category_id)
        if category is None:
            return None

        # Обновление названия и описания, если они переданы
        if title:
            category.title = title

        # Сохранение изменений в базе данных
        db.update_category(category)

        return category

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None):
        task = sql.db_categories.get_task_from_db_by_id(task_id)
        if task is None:
            return None

        # Обновление названия и описания, если они переданы
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        # Сохранение изменений в базе данных
        db.update_task(task)

        return task

categories_service: CategoriesService = CategoriesService()
