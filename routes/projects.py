from fastapi import APIRouter

from services.projects import createProject

from schemas.projects import createProjectSchema

router = APIRouter()

@router.get('/')
def home():
    return "PROJECTS"

@router.post('/')
def projectCreate(project: createProjectSchema):
    projectid = createProject(project)

    return {
        "success": True,
        "message": "Created project successfully!",
        "projectid": projectid
    }