from project_services import create_project, find_project_by_title

projects = []
app_running = True

while app_running:

    print("=== Mythos Labs ===\n")
    print("1 - Register project")
    print("2 - Search project")
    print("3 - List project")
    print("4 - Exit\n")
    choice = input("Choose an action: ")

    


    #REGISTER A PROJECT
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
        
        #LIST ALL PROJECTS
        print("\nRegistered Projects:\n")
        for project in projects:
            print(f"Title: {project['title']}")
            print(f"Author: {project['author']}\n")
        
        #SEARCH FOR A PROJECT
        title_search = input("Search project by title: ")
        title_search_result = find_project_by_title(projects, title_search)
        if title_search_result == None:
            print("Project not found.")
        else:
            print(title_search_result)
        
        app_running = False
    
    except ValueError:
        print("Error: Not an integer number.")
            

        
