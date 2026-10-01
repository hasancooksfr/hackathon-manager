from fastapi import APIRouter

from services.members import createMember

from schemas.members import createMemberSchema

router = APIRouter()

@router.get('/')
def membersHome():
    return "Members"

@router.post('/')
def memberCreate(data: createMemberSchema):
    createMember(data)

    return {
        "success": True,
        "message": "Member created successfully!"
    }