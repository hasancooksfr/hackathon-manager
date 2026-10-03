from fastapi import APIRouter

from services.projects import createProject
from services.projects import getAllProjects
from services.projects import getProjectsByTeam
from services.projects import getProjectData
from services.projects import getProjectByQuerySearch
from services.projects import updateProjectData
from services.projects import deleteProject
from services.projects import addDevLog
from services.projects import getDevLogs

from schemas.projects import createProjectSchema
from schemas.projects import updateProjectSchema
from schemas.projects import DevLogSchema

router = APIRouter()

@router.get('/')
def home():
    data= getAllProjects()

    return {
        "success": True,
        "message": "Fetched all projects!",
        "data": data
    }

@router.post('/')
def projectCreate(project: createProjectSchema):
    projectid = createProject(project)

    return {
        "success": True,
        "message": "Created project successfully!",
        "projectid": projectid
    }

@router.get('/team/{teamid}')
def projectByTeam(teamid):
    data = getProjectsByTeam(teamid)

    return {
        "success": True,
        "message": "Fetched all projects by teamid!",
        "data": data
    }

@router.get('/{projectid}')
def projectData(projectid):
    return getProjectData(projectid)

@router.get('/search/')
def searchProject(
    name: str = None,
    status: str = None
):
    data = getProjectByQuerySearch(name, status)

    return {
        "success": True,
        "message": "Fetched all projects by search!",
        "data": data
    }

@router.put('/{projectid}')
def updateProject(projectid, project: updateProjectSchema):
    updateProjectData(projectid, project)

    return {
        "success": True,
        "message": "Updated project data successfully!",
        "projectid": projectid
    }

@router.delete('/{projectid}')
def delProject(projectid):
    deleteProject(projectid)

    return {
        "success": True,
        "message": "Deleted project successfully!"
    }
@router.post('/devlog/{projectid}')
def LogDevlog(projectid, devlog: DevLogSchema):
    addDevLog(projectid, devlog)

    return {
        "success": True,
        "message": "Added Devlog to project!"
    }

@router.get('/devlog/{projectid}')
def fetchDevlogs(projectid):
    data = getDevLogs(projectid)

    return {
        "success": True,
        "message": "Fetched all devlogs with projectid.",
        "data": data
    }