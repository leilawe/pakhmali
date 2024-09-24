projects= {}

def add_project():
    project_name =input("Enter your project name: ")
    if project_name in projects:
        print(" project already existes. ")
        return
    deadline=input("Enter project deadline (YYYY-MM-DD): ")
    status= input(" Enter project status (e.g, ongoing, completed, etc.): ")
    projects[project_name]={"deadline":deadline, "status":status, "obligations":[]}
    print(f" The {project_name} project added successfully")

def edit_project():
    project_name=input(" Enter the project name to edit: ")
    if project_name not in projects:
        print(" Project not found! ")
        return
    deadline=input(f" Enter new deadline for {project_name}: ")
    status=input(f" Enter new status for {project_name}: ")
    projects[project_name]["deadline"]= deadline
    projects[project_name]["status"]= status
    print(f"Project {project_name} edited successfully. ")

def delete_project():
    project_name=input(" Enter the project name to delete: ")
    if project_name in projects:
        del projects[project_name]
        print(f"Project {project_name} deleted. ")
    else:
        print(" Project not found! ")

def add_obligation():
    project_name=input(" Enter the project name to add obligation: ")
    if project_name not in projects:
        print(" Project not found! ")
        return
    obligation=input(" Enter the obligation: ")
    projects[project_name]["obligations"].append(obligation)
    print(f" obligation added to {project_name}.")

def edit_obligation():
  project_name = input("Enter the project name to edit obligation: ")
  if project_name not in projects:
        print("Project not found.")
        return
  obligations = projects[project_name]["obligations"]
  if not obligations:
        print("No obligations found for this project.")
        return
    
  counter = 1
  for obligation in obligations:
        print(f"{counter}. {obligation}")
        counter += 1

  obligation_index = int(input("Enter the number of the obligation to edit: ")) - 1
  if obligation_index < 0 or obligation_index >= len(obligations):
        print("Invalid obligation number.")
        return
    
  new_obligation = input("Enter the new obligation: ")
  obligations[obligation_index] = new_obligation
  print("Obligation updated.")  

def delete_obligation():
    project_name = input("Enter the project name to delete obligation: ")
    if project_name not in projects:
        print("Project not found.")
        return
    obligations = projects[project_name]["obligations"]
    if not obligations:
        print("No obligations found for this project.")
        return

    counter = 1
    for obligation in obligations:
        print(f"{counter}. {obligation}")
        counter += 1

    obligation_index = int(input("Enter the number of the obligation to delete: ")) - 1
    if obligation_index < 0 or obligation_index >= len(obligations):
        print("Invalid obligation number.")
        return

    del obligations[obligation_index]
    print("Obligation deleted.")

def display_projects():
    if not projects:
        print("No projects available.")
        return
    for project_name, project_info in projects.items():
        print(f"\nProject: {project_name}")
        print(f"  Deadline: {project_info["deadline"]}")
        print(f"  Status: {project_info["status"]}")
        print("  Obligations:")
        if project_info["obligations"]:
            for obligation in project_info["obligations"]:
                print(f"  {obligation}")
        else:
            print(" No obligations.")

def menu():
    while True:
        print("\nProject Management System")
        print("1. Add Project")
        print("2. Edit Project")
        print("3. Delete Project")
        print("4. Add Obligation")
        print("5. Edit Obligation")
        print("6. Delete Obligation")
        print("7. Display Projects")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_project()
        elif choice == "2":
            edit_project()
        elif choice == "3":
            delete_project()
        elif choice == "4":
            add_obligation()
        elif choice == "5":
            edit_obligation()
        elif choice == "6":
            delete_obligation()
        elif choice == "7":
            display_projects()
        elif choice == "8":
            print("Exiting the program. ")
            break
        else:
            print("Invalid option. Please choose again.")


menu()
