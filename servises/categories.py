from __future__ import annotations

import json
from typing import List

import sql.db_categories as db
import sql.db_users as db_us
from  schemas.categories import CategoriesCreate, Categories
import uuid


class CategoriesService:


    def categories_create(self, data: CategoriesCreate) ->CategoriesCreate:
        categ = Categories(
            id = uuid.uuid4().__str__(),
            title = data.title,
            tasks = 1
        )
        return db.createCategories(categ)

    def categories_get(self):
        return db.get_categories()

categories_service: CategoriesService = CategoriesService()
