def describe_project(title, author):
    return f"Project '{title}' was created by {author}"

sentence = []

quantity_input = input("How many projects do you want to register? ")

try:
    quantity = int(quantity_input)
    for i in range (quantity):
        title_input = input("Enter project title: ")
        author_input = input("Enter author name: ")
        if not title_input and not author_input:
            print("Error: 'Project title' AND 'author' cannot be empty.")
        elif not title_input:
            print("Error: Project title cannot be empty.")
        elif not author_input:    
            print("Error: Author cannot be empty.")  
        else:
            project_info = describe_project(title_input, author_input)
            sentence.append(project_info)
    print(f"Registered products:\n{'\n'.join(sentence)}") 
except ValueError:
    print("Not an integer number.")    


   
