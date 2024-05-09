from __future__ import annotations

import json
from typing import List

import sql.db_categories as db
import sql.db_users as db_us
from schemas.categories import CategoriesCreate, Categories, TaskCreate, Task
import uuid
from typing import Optional


class CategoriesService:

    def categories_create(self, data: CategoriesCreate) -> CategoriesCreate:
        categ = Categories(
            id=str(uuid.uuid4()), title=data.title, tasks=[])
        return db.createCategories(categ)

    def categories_get(self):
        return db.get_categories()

    def task_create(self, data: TaskCreate) -> Task:
        task = Task(
            id=str(uuid.uuid4()), title=data.title, description=data.description, category_id=data.category_id)
        return db.createTask(task)

    def get_category_by_id(self, category_id: str) -> Optional[Categories]:
        category = db.get_category_by_id(db.session, category_id)
        if category:
            return Categories(id=category.id, title=category.title, tasks=[])
        return None


categories_service: CategoriesService = CategoriesService()
