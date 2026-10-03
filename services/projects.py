from fastapi import HTTPException
from database import members_collection, projects_collection, teams_collection

def createProject(project):
    project = project.model_dump()

    team = teams_collection.find_one(
        {
            "teamid": project['teamid']
        }
    )
    if not team:
        raise HTTPException(
            status_code=404,
            detail="No records found for teamid."
        )

    project['status'] = "working"
    project['devlogs'] = {}

    last_project = projects_collection.find_one(
        {},
        sort=[("projectid", -1)]
    )
    if not last_project:
        project_id = "PROJ0001"

    else:
        last_id = int(last_project['projectid'].replace("PROJ", ""))
        project_id = f"PROJ{last_id+1:04d}"

    project['projectid'] = project_id

    projects_collection.insert_one(
        project
    )

    return project_id

def getAllProjects():
    data = list(
        projects_collection.find(
            {},
            {
                "_id": 0,
                "projectid": 1,
                "teamid": 1,
                "name": 1
            }
        )
    )

    return data

def getProjectsByTeam(teamid):
    data = list(
        projects_collection.find(
            {
                "teamid": teamid
            },
            {
                "_id": 0,
                "projectid": 1,
                "teamid": 1,
                "name": 1
            }
        )
    )

    return data

def getProjectData(projectid):
    data = projects_collection.find_one(
        {
            "projectid": projectid
        },
        {
            "_id": 0
        }
    )
    if not data:
        raise HTTPException(
            status_code=404,
            detail="No records found for projectid."
        )

    return data

def getProjectByQuerySearch(
    name: str = None,
    status: str = None
):
    query = {}

    if name:
        query['name'] = name

    if status:
        query['status'] = status

    data = list(projects_collection.find(
        query,
        {
            "_id": 0,
            "projectid": 1,
            "teamid": 1,
            "name": 1
        }
    ))

    return data

def updateProjectData(projectid, project):
    project = project.model_dump(exclude_unset=True)

    res = projects_collection.update_one(
        {
            "projectid": projectid
        },
        {
            "$set": project
        }
    )

    if res.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for projectid."
        )

    return True

def deleteProject(projectid):
    res = projects_collection.delete_one(
        {
            "projectid": projectid
        }
    )
    if res.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for projectid."
        )

    return True