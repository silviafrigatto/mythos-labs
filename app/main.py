from project_services import create_project

projects = []
app_running = True

while app_running:
    quantity_input = input("How many projects do you want to register? ")
    try:
        quantity = int(quantity_input)
        while quantity > 0:
            title_input = input("Enter project title: ")
            author_input = input("Enter author name: ")
            if not title_input or not author_input:
                print("Error: 'Project title' and/or 'author' cannot be empty.")
                continue
            project = create_project(title_input, author_input)
            projects.append(project)
            quantity -= 1
        print("\nRegistered Projects:\n")
        for project in projects:
            print(f"Title: {project['title']}")
            print(f"Author: {project['author']}\n")
        app_running = False
    except ValueError:
        print("Error: Not an integer number.")
            

        
