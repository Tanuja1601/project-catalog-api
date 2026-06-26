from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:
    @staticmethod
    def list_projects(session: Session) -> list[Project]:
        return session.query(Project).order_by(Project.updated_at.desc()).all()

    @staticmethod
    def get_project(session: Session, project_id: int) -> Project | None:
        return session.get(Project, project_id)

    @staticmethod
    def create_project(session: Session, payload: ProjectCreate) -> Project:
        project = Project(**payload.model_dump(mode="json"))
        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    @staticmethod
    def update_project(session: Session, project: Project, payload: ProjectUpdate) -> Project:
        for field_name, value in payload.model_dump(mode="json").items():
            setattr(project, field_name, value)
        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    @staticmethod
    def delete_project(session: Session, project: Project) -> None:
        session.delete(project)
        session.commit()
