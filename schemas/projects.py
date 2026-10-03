from pydantic import BaseModel, Field

class createProjectSchema(BaseModel):
    teamid: str
    name: str
    description: str

class updateProjectSchema(BaseModel):
    name: str | None = None
    description: str | None = None