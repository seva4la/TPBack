from typing import List

from fastapi import HTTPException
from sqlalchemy import create_engine, Column, String, Boolean, ForeignKey, Integer, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from sql.db_users import TableUser

from schemas.categories import CategoriesCreate, Categories

Base = declarative_base()


class TableCategories(Base):
    __tablename__ = "categories"
    id = Column("id", String, primary_key=True)
    title = Column("title", String)
    tasks = Column("tasks", String)


engine = create_engine("sqlite:///db/categories.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


def test_to_table_test(categ: Categories) -> TableCategories:
    return TableCategories(
        id=categ.id,
        title=categ.title,
        tasks=categ.tasks
    )

def table_to_categories(categories: TableCategories) -> Categories:
    return Categories(
        id=categories.id,
        title=categories.title,
        tasks=categories.tasks
    )

def createCategories(categ: Categories) -> Categories:
    table_test = test_to_table_test(categ)
    session.add(table_test)
    session.commit()
    return categ


def get_categories():
    list_test = session.query(TableCategories).all()
    list_test_mas = []
    for item in list_test:
        list_test_mas.append(table_to_categories(item))
    return list_test