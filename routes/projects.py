from fastapi import APIRouter

from services.projects import createProject
from services.projects import getAllProjects

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