from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.services.project_service import ProjectService


router = APIRouter(prefix="/projects")


@router.get("", response_model=list[ProjectRead])
def list_projects(session: Session = Depends(get_session)) -> list[ProjectRead]:
    return ProjectService.list_projects(session)


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, session: Session = Depends(get_session)) -> ProjectRead:
    project = ProjectService.get_project(session, project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate, session: Session = Depends(get_session)) -> ProjectRead:
    return ProjectService.create_project(session, payload)


@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, payload: ProjectUpdate, session: Session = Depends(get_session)) -> ProjectRead:
    project = ProjectService.get_project(session, project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return ProjectService.update_project(session, project, payload)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, session: Session = Depends(get_session)) -> Response:
    project = ProjectService.get_project(session, project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    ProjectService.delete_project(session, project)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
