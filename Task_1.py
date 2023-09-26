# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task, priority):
    todo_list.append({'Task': task, 'Priority': priority})

# Function to display the to-do list
def display_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, item in enumerate(todo_list):
            print(f"{i + 1}. Task: {item['Task']} | Priority: {item['Priority']}")

# Function to update a task's priority
def update_priority(task_index, new_priority):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]['Priority'] = new_priority
        print("Task priority updated.")
    else:
        print("Invalid task index. No task updated.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task['Task']}' removed.")
    else:
        print("Invalid task index. No task removed.")

# Main application loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Display to-do list")
    print("3. Update task priority")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter the task: ")
        priority = input("Enter the priority (High/Medium/Low): ")
        add_task(task, priority)
        print("Task added to the to-do list.")
    elif choice == '2':
        display_list()
    elif choice == '3':
        task_index = int(input("Enter the index of the task to update: "))
        new_priority = input("Enter the new priority (High/Medium/Low): ")
        update_priority(task_index - 1, new_priority)
    elif choice == '4':
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index - 1)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")