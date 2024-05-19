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
    color = Column("column", String)
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
                           user_id=task.user_id, color=task.color)
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
                                      category_id=item.category_id, color=item.color))
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

def delete_task_by_id(task_id: str):
    task = session.query(TableTask).filter(TableTask.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()

def get_task_from_db_by_id(task_id: str):
    return session.query(TableTask).filter(TableTask.id == task_id).first()

def delete_category_and_tasks(category_id: str):
    category = session.query(TableCategories).filter(TableCategories.id == category_id).first()
    if category:
        session.delete(category)
        session.commit()

def update_category(category: Categories):
    category_in_db = session.query(TableCategories).filter(TableCategories.id == category.id).first()
    if category_in_db:
        if category.title:
            category_in_db.title = category.title
        session.commit()

def update_task(task: Task):
    task_in_db = session.query(TableTask).filter(TableTask.id == task.id).first()
    if task_in_db:
        if task.title is not None:
            task_in_db.title = task.title
        if task.description is not None:
            task_in_db.description = task.description
        session.commit()