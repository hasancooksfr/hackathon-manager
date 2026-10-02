from pydantic import BaseModel, Field   

class createMemberSchema(BaseModel):
    name: str
    email_id: str
    contact_number: int
    slack_id: str
    github_id: str