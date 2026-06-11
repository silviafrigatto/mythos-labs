def show_menu():
    print("=== Mythos Labs ===\n")
    print("1 - Register project")
    print("2 - Search project")
    print("3 - List project")
    print("4 - Exit\n")

def create_project(title, author):
    return {
        "title": title,
        "author": author
    }

def find_project_by_title(projects, title):
   return next((project for project in projects if project.get('title') == title), None) 