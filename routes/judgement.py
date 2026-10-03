from fastapi import APIRouter

from services.judgement import approveProject

from schemas.judgement import approveProjectSchema

router = APIRouter()

@router.get('/')
def home():
    return "JUDGEMENT SYSTEM"

@router.put('/approve/{projectid}')
def projectApprove(projectid, review: approveProjectSchema):
    approveProject(projectid, review)

    return {
        "success": True,
        "message": "Approved project successfully!",
        "projectid": projectid
    }