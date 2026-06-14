from fastapi import FastAPI
from app.project_services import find_project_by_title

app = FastAPI()

projects = [
    {
        "title": "Echoes of Ithaca",
        "author": "Helena"
    },
    {
        "title": "The Last Oracle",
        "author": "Marcus"
    }
]

@app.get("/")
def home():
    return {"message": "Welcome to Mythos Labs"}

@app.get("/projects")
def get_projects():
    return projects

@app.get("/projects/{title}")
def get_projects_by_title(title:str):
    return find_project_by_title(projects, title)