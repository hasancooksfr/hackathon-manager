from fastapi import FastAPI

from routes.members import router as members_router
from routes.members import router as teams_router

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