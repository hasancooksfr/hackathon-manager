from pydantic import BaseModel, Field

class createTeamSchema(BaseModel):
    name: str
    leader_id: str

class updateTeamSchema(BaseModel):
    name: str | None = None
    leader_id: str | None = None