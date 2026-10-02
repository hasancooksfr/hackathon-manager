from fastapi import APIRouter

from services.members import createMember
from services.members import getAllMembers

from schemas.members import createMemberSchema

router = APIRouter()

@router.get('/')
def membersHome():
    data = getAllMembers()

    return {
        "success": True,
        "message": "Fetched all members",
        "data": data
    }

@router.post('/')
def memberCreate(data: createMemberSchema):
    createMember(data)

    return {
        "success": True,
        "message": "Member created successfully!"
    }
