from app.project_services import create_project

def test_create_project():
    project = create_project(
        "Echoes of Ithaca",
        "Helena"
    )

    assert project['title'] == "Echoes of Ithaca"
    assert project['author'] == "Helena"