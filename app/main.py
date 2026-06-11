from project_services import show_menu, create_project, find_project_by_title

projects = []
search = True
    
while True:
    show_menu()
    register = True
    choice = input("Enter your choice (1 - 4): ")
    if choice == "1":
        while register:
            print("\n=== Register project ===\n")
            quantity_input = input("How many projects do you want to register? ")
            try:
                quantity = int(quantity_input)
                while quantity > 0:
                    title_input = input("\nEnter project title: ")
                    author_input = input("Enter author name: ")
                    if not title_input or not author_input:
                        print("ERROR: 'Project title' and/or 'author' cannot be empty.")
                        continue
                    project = create_project(title_input, author_input)
                    projects.append(project)
                    quantity -= 1   
                print("\nProjects successfully registered!\n")
                register = False
            except ValueError:
                print("ERROR: Not an integer number. Please try again.")
    elif choice == "2":
        while search:
            print("\n=== Search project ===\n")
            title_search = input("Search project by title: ")
            title_search_result = find_project_by_title(projects, title_search)
            if title_search_result == None:
                print("Project not found.\n")
            else:
                print(title_search_result)
                search = False
    elif choice == "3":
        print("\n=== List projects ===\n")
        if not projects:
            print("There are no projects registered yet.\n")
        else:
            print("\nRegistered Projects:\n")
            for project in projects:
                print(f"Title: {project['title']}")
                print(f"Author: {project['author']}\n")
    elif choice == "4":
        exit()
    else:
        print("\nERROR: Invalid selection. Please try again.\n")
    
    
            

        
