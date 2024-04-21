from fastapi import APIRouter
from typing import List, Union
from schemas.projects_schema import Project, ProjectCreate
from schemas.schemas import  Response
from services.manage_projects import project_service
router = APIRouter()

@router.get(
    "/projects",
    status_code=200,
    response_model=list[Project]
)
def get_projects():
    return project_service.get_projects()


@router.post("/add_project/{proj_id}", response_model=Response)
def make_project(data: ProjectCreate):
    return project_service.make_project(data)

@router.put(
    "/project/{id}",response_model=Response
)
def delete_project(
        id: int):
    return project_service.delete_project(id)

@router.get(
    "/show_tasks",response_model=Union[List[int], None]
)
def show_tasks(
        proj_id: int):
    return project_service.show_tasks(proj_id)