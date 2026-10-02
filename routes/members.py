from fastapi import APIRouter

from services.members import createMember
from services.members import getAllMembers
from services.members import getMembersByQuery

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

@router.get('/search')
def searchMembers(
    name: str = None,
    email_id: str = None,
    contact_number: int = None,
    slack_id: str = None,
    github_id: str = None
):
    data = getMembersByQuery(name, email_id, contact_number, slack_id, github_id)

    return {
        "success": True,
        "message": "Fetched members with given query.",
        "data": data
    }