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
            user_id=data.user_id)
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

categories_service: CategoriesService = CategoriesService()
