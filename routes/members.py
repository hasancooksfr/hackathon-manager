from fastapi import APIRouter

from services.members import createMember
from services.members import getAllMembers
from services.members import getMembersByQuery
from services.members import getMemberData
from services.members import updateMember
from services.members import deleteMember

from schemas.members import createMemberSchema
from schemas.members import updateMemberSchema

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

@router.get('/{memberid}')
def getMember(memberid: str):
    return getMemberData(memberid)

@router.put('/{memberid}')
def memberUpdate(memberid: str, member: updateMemberSchema):
    updateMember(memberid, member)

    return {
        "success": True,
        "message": "Updated member successfully!",
        "memberid": memberid
    }

@router.delete('/{memberid}')
def memberDelete(memberid: str):
    deleteMember(memberid)

    return {
        "success": True,
        "message": "Deleted member successfully!",
        "memberid": memberid
    }