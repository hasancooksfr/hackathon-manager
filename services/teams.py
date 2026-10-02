from fastapi import HTTPException
from database import members_collection, teams_collection

def createTeam(team):
    team = team.model_dump()

    leader = members_collection.find_one(
        {
            "memberid": team['leader_id']
        }
    )
    if not leader:
        raise HTTPException(
            status_code=404,
            detail="No records found for leader_id."
        )

    leader_team = teams_collection.find_one(
        {
            "team_members": team['leader_id']
        }
    )
    if leader_team:
        raise HTTPException(
            status_code=409,
            detail="Leader is already in another team."
        )

    last_team = teams_collection.find_one(
        {},
        sort=[("teamid", -1)]
    )

    if not last_team:
        teamid = "TEAM0001"
    else:
        last_id = int(last_team['teamid'].replace("TEAM", ""))
        teamid = f"TEAM{last_id+1:04d}"

    data = {
        "teamid": teamid,
        "name": team['name'],
        "leader_id": team['leader_id'],
        "team_members": [
            team['leader_id']
        ]
    }
    teams_collection.insert_one(data)

    return teamid

def getAllTeams():
    data = list(teams_collection.find(
        {},
        {
            "_id": 0,
            "teamid": 1,
            "name": 1,
            "leader_id": 1
        }
    ))

    return data

def getTeamsBySearch(
    name: str = None,
    member_id: str = None
):
    query = {}

    if name:
        query['name'] = name

    if member_id:
        query['team_members'] = member_id

    data = list(teams_collection.find(
        query,
        {
            "_id": 0,
            "teamid": 1,
            "name": 1,
            "leader_id": 1
        }
    ))

    return data

def getTeamData(teamid):
    data = teams_collection.find_one(
        {
            "teamid": teamid
        },
        {
            "_id": 0
        }
    )

    if not data:
        raise HTTPException(
            status_code=404,
            detail="No records found for teamid."
        )

    return data

def updateTeamData(teamid, team):
    team = team.model_dump(exclude_unset=True)

    if team['leader_id']:
        leader = members_collection.find_one(
            {
                "memberid": team['leader_id']
            }
        )
        if not leader:
            raise HTTPException(
                status_code=404,
                detail="No records found for leader_id."
            )

        existing = teams_collection.find_one(
            {
                "team_members": team['leader_id'],
                "teamid": {"$ne": teamid}
            }
        )
        if existing:
            raise HTTPException(
                status_code=409,
                detail="Leader is already in another team."
            )

    res = teams_collection.update_one(
        {
            "teamid": teamid
        },
        {
            "$set": team
        }
    )

    if res.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for teamid."
        )

    return True

def deleteTeam(teamid):
    res = teams_collection.delete_one(
        {
            "teamid": teamid
        }
    )
    if res.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for teamid."
        )

    return True