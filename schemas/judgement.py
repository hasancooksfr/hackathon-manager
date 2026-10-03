from pydantic import BaseModel

class reviewProjectSchema(BaseModel):
    reviewer_name: str
    remarks: str