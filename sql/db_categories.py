from typing import List
from fastapi import HTTPException
from sqlalchemy import create_engine, Column, String, Boolean, ForeignKey, Integer, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sql.db_users import TableUser
import uuid
from schemas.categories import CategoriesCreate, Categories, TaskCreate, Task
Base = declarative_base()
from schemas.users import User


class TableTask(Base):
    __tablename__ = "tasks"
    id = Column("id", String, primary_key=True)
    title = Column("title", String)
    description = Column("description", String)
    user_id = Column("user_id", String)
    category_id = Column(String, ForeignKey("categories.id"))
    category = relationship("TableCategories", back_populates="tasks")

class TableCategories(Base):
    __tablename__ = "categories"
    id = Column("id", String, primary_key=True)
    title = Column("title", String)
    user_id = Column("user_id", String)
    tasks = relationship("TableTask", back_populates="category")

engine = create_engine("sqlite:///db/categories.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


# def test_to_table_test(categ: Categories) -> TableCategories:
#     return TableCategories(
#         id=categ.id,
#         title=categ.title,
#         tasks=categ.tasks
#     )
#
# def table_to_categories(categories: TableCategories) -> Categories:
#     return Categories(
#         id=categories.id,
#         title=categories.title,
#         tasks=categories.tasks
#     )



def createCategories(categ: Categories) -> Categories:
    table_test = TableCategories(id=categ.id, title=categ.title, user_id=categ.user_id)
    session.add(table_test)
    session.commit()
    return categ

def createTask(task: Task) -> Task:
    category = get_category_by_id(session, task.category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    table_test = TableTask(id=task.id, title=task.title, description=task.description, category_id=task.category_id,
                           user_id=task.user_id)
    session.add(table_test)
    session.commit()
    return task


def get_categories_with_id(user: User):
    list_test = session.query(TableCategories).all()
    list_test_mas = []
    for item in list_test:
        if (item.user_id == user.id):
            tasks = []
            for task in item.tasks:
                tasks.append(Task(**task.__dict__))
            list_test_mas.append(Categories(id=item.id, title=item.title, user_id=item.user_id, tasks=tasks))
    return list_test_mas


def get_task_with_id(user: User):
    list_test = session.query(TableTask).all()
    list_test_mas = []
    for item in list_test:
        if (item.user_id == user.id):
            list_test_mas.append(Task(id=item.id, title=item.title, user_id=item.user_id, description=item.description,
                                      category_id=item.category_id))
    return list_test_mas


def get_categories():
    list_test = session.query(TableCategories).all()
    list_test_mas = []
    for item in list_test:
        tasks = []
        for task in item.tasks:
            tasks.append(Task(**task.__dict__))
        list_test_mas.append(Categories(id=item.id, title=item.title, user_id=item.user_id, tasks=tasks))
    return list_test_mas

def get_category_by_id(db: Session, category_id: str):
    return db.query(TableCategories).filter(TableCategories.id == category_id).first()

