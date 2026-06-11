from app.project_services import create_project, find_project_by_title, show_project_info

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
   assert project['author'] == "Helena"

def test_show_project_info(capsys):
    project = {"title": "Echoes of Ithaca", "author": "Helena"}
    show_project_info(project)
    captured = capsys.readouterr()

    assert captured.out == (
        "Title: Echoes of Ithaca\n"
        "Author: Helena\n\n"
    )
