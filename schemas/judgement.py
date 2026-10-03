from pydantic import BaseModel

class approveProjectSchema(BaseModel):
    reviewer_name: str
    remarks: str