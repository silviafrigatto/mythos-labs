from app.project_services import create_project, find_project_by_title

def test_create_project():
    project = create_project(
        "Echoes of Ithaca",
        "Helena"
    )

    assert project['title'] == "Echoes of Ithaca"
    assert project['author'] == "Helena"

def test_find_project_by_title():
   projects = [{"title": "Echoes of Ithaca", "author": "Helena"}]
   project = find_project_by_title(projects, "Echoes of Ithaca")
   
   assert project['title'] == "Echoes of Ithaca"


