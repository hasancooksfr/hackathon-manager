from fastapi import APIRouter

from services.judgement import approveProject
from services.judgement import rejectProjectwithRemarks

from schemas.judgement import reviewProjectSchema

router = APIRouter()

@router.get('/')
def home():
    return "JUDGEMENT SYSTEM"

@router.put('/approve/{projectid}')
def projectApprove(projectid, review: reviewProjectSchema):
    approveProject(projectid, review)

    return {
        "success": True,
        "message": "Approved project successfully!",
        "projectid": projectid
    }

@router.put('/changes-req/{projectid}')
def changesRequest(projectid, review: reviewProjectSchema):
    rejectProjectwithRemarks(projectid, review)

    return {
        "success": True,
        "message": "Rejected project with requesting changes successfully!",
        "projectid": projectid
    }