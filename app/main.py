def describe_project(title, author):
    return f"Project '{title}' was created by {author}"

sentence = []
run_app = True

while run_app:
    quantity_input = input("How many projects do you want to register? ")
    try:
        quantity = int(quantity_input)
        while quantity > 0:
            title_input = input("Enter project title: ")
            author_input = input("Enter author name: ")
            if not title_input or not author_input:
                print("Error: 'Project title' and/or 'author' cannot be empty.")
                continue
            project_info = describe_project(title_input, author_input)
            sentence.append(project_info)
            print(sentence)
            quantity -= 1
        run_app = False
    except ValueError:
        print("Error: Not an integer number.")

        
                
        #for i in range (quantity):
        #    title_input = input("Enter project title: ")
        #    author_input = input("Enter author name: ")
        #    if not title_input or not author_input:
        #        print("Error: 'Project title' and/or 'author' cannot be empty.")
            #elif not title_input:
            #    print("Error: Project title cannot be empty.")
            #elif not author_input:    
            #    print("Error: Author cannot be empty.")  
        #    else:
        #        project_info = describe_project(title_input, author_input)
        #        sentence.append(project_info)
        #print(f"Registered products:\n{'\n'.join(sentence)}") 
        #print(sentence)
            

        
