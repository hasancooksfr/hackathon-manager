from fastapi import APIRouter

from services.projects import createProject
from services.projects import getAllProjects
from services.projects import getProjectsByTeam
from services.projects import getProjectData

from schemas.projects import createProjectSchema

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