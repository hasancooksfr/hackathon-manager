from pydantic import BaseModel, Field   

class createMemberSchema(BaseModel):
    name: str
    email_id: str
    contact_number: int
    slack_id: str
    github_id: str

class updateMemberSchema(BaseModel):
    name: str | None = None
    email_id: str | None = None
    contact_number: int | None = None
    slack_id: str | None = None
    github_id: str | None = None