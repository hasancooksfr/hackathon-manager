from fastapi import FastAPI

from routes.members import router as members_router
from routes.teams import router as teams_router
from routes.judgement import router as judgement_router
from routes.projects import router as projects_router

app = FastAPI()

@app.get('/')
def home():
    return "HOME"

app.include_router(
    members_router,
    prefix="/members",
    tags=['Members']
)

app.include_router(
    teams_router,
    prefix="/teams",
    tags=['Teams']
)

app.include_router(
    projects_router,
    prefix="/projects",
    tags=['Projects']
)

app.include_router(
    judgement_router,
    prefix="/judgement",
    tags=['Judgement']
)