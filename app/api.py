from fastapi import FastAPI
from project_services import find_project_by_title

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

search = "Echoes of Ithaca"
title = find_project_by_title(projects, search)

@app.get("/")
def home():
    return {"message": "Welcome to Mythos Labs"}

@app.get("/projects")
def get_projects():
    return projects

@app.get("/projects/{title}")
def get_projects(title:str):
    return title