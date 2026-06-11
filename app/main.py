from project_services import show_menu, create_project, find_project_by_title

projects = []
app_running = True

while app_running:

    
    while True:
        show_menu()

        choice = input("Enter your choice (1 - 4): ")
        if choice == "1":
            print("===Register project===\n")
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
                
                app_running = False
            except ValueError:
                print("ERROR: Not an integer number.")
        elif choice == "2":
            print("===Search project===\n")
            title_search = input("Search project by title: ")
            title_search_result = find_project_by_title(projects, title_search)
            if title_search_result == None:
                print("Project not found.")
            else:
                print(title_search_result)
        elif choice == "3":
            print("List project")
        elif choice == "4":
            print("Exit")
        else:
            print("\nERROR: Invalid selection. Please try again.\n")
    
    
            

        
