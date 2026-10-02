from pydantic import BaseModel, Field

class createProjectSchema(BaseModel):
    teamid: str
    name: str
    description: str