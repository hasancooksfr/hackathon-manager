from fastapi import APIRouter

from services.teams import createTeam

from schemas.teams import createTeamSchema

router = APIRouter()

@router.get('/')
def home():
    return "TEAMS"

@router.post('/')
def teamCreate(team: createTeamSchema):
    teamid = createTeam(team)

    return {
        "success": True,
        "message": "Created team successfully!",
        "teamid": teamid
    }