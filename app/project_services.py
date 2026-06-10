def create_project(title, author):
    return {
        "title": title,
        "author": author
    }

def find_project_by_title(projects, title):
   return next((project for project in projects if project.get('title') == title), None) 