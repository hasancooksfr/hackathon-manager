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