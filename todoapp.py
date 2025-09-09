tasks = []

def show_menu():
    print("Menu:")
    print("Select an option")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Please enter your task: ")
    if task == "":
        print("Please add a task")
    else:
        tasks.append(task)
        print(f"Task '{task}' added.")

def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks to view.")
        return

    print("Here are your tasks:")
    i = 0
    while i < len(tasks):
        print(i + 1, "-", tasks[i])
        i = i + 1

        

running = True
while running:
    show_menu()
    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Delete task not built yet")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("That choice does not exist. Please pick options 1, 2, 3, or 4.")
