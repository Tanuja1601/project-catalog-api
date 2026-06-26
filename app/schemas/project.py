from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class ProjectBase(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    summary: str = Field(min_length=10, max_length=2000)
    tech_stack: list[str] = Field(default_factory=list)
    repo_url: HttpUrl | None = None
    live_url: HttpUrl | None = None
    is_featured: bool = False


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
