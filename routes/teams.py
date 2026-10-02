from fastapi import APIRouter

from services.teams import createTeam
from services.teams import getAllTeams
from services.teams import getTeamsBySearch
from services.teams import getTeamData
from services.teams import updateTeamData
from services.teams import deleteTeam

from schemas.teams import createTeamSchema
from schemas.teams import updateTeamSchema

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

@router.get('/search')
def searchTeam(
    name: str = None,
    member_id: str = None
):
    data = getTeamsBySearch(name, member_id)

    return {
        "success": True,
        "message": "Fetched teams with given query",
        "data": data
    }

@router.get('/{teamid}')
def teamData(teamid: str):
    return getTeamData(teamid)

@router.put('/{teamid}')
def teamUpdate(teamid: str, team: updateTeamSchema):
    updateTeamData(teamid, team)

    return {
        "success": True,
        "message": "Updated team information successfully!",
        "teamid": teamid
    }

@router.delete('/{teamid}')
def teamDelete(teamid: str):
    deleteTeam(teamid)

    return {
        "success": True,
        "message": "Deleted team successfully!"
    }