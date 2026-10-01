from fastapi import FastAPI

from routes.members import router as members_router

app = FastAPI()

@app.get('/')
def home():
    return "HOME"

app.include_router(
    members_router,
    prefix="/members",
    tags=['Members']
)