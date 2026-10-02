from fastapi import APIRouter

from services.teams import createTeam
from services.teams import getAllTeams

from schemas.teams import createTeamSchema

router = APIRouter()

@router.get('/')
def home():
    data = getAllTeams()

    return {
        "success": True,
        "message": "Fetched all teams!",
        "data": data
    }

@router.post('/')
def teamCreate(team: createTeamSchema):
    teamid = createTeam(team)

    return {
        "success": True,
        "message": "Created team successfully!",
        "teamid": teamid
    }

