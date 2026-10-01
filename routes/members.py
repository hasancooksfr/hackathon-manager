from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def membersHome():
    return "Members"