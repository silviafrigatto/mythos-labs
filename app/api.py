from fastapi import FastAPI

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