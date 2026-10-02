from pydantic import BaseModel, Field

class createTeamSchema(BaseModel):
    name: str
    leader_id: str