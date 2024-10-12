import json #for saving and loading the file 

# intialising a class name task
class Task:
    def __init__(self, title, description, category):
        self.title = title # the name of the task
        self.description = description # detailed discription of the task
        self.category = category  # category of the task
        self.completed = False # used to determine weather the task is complete or not 

    def mark_completed(self): # function for complted task
        self.completed = True

    def to_dict(self): # function to convert task into dictionary
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):  # function to conert dictionary back into task when reading from a file
        task = Task(data["title"], data["description"], data["category"])
        task.completed = data["completed"]
        return task


# function to save tasks in to JSON file
def save_tasks(tasks): 
    with open('tasks.json', 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)


# function to load tasks fron JSON file 
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        return []


# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print(f"Task '{title}' added successfully!")


# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx}. [{status}] {task.title} - {task.category}")
        print(f"   Description: {task.description}")


# Function to mark a task as completed
def mark_task_completed(tasks):
    if not tasks:
        print("No tasks to mark as completed.")
        return

    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as completed: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1].mark_completed()
        print(f"Task '{tasks[task_num - 1].title}' marked as completed!")
    else:
        print("Invalid task number.")


# Function to delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task.title}' deleted!")
    else:
        print("Invalid task number.")


# Main function to run the To-Do List Application
def main():
    tasks = load_tasks()

    while True:
        print("\n-- To-Do List Application --") 
        print("1. Add Task") # to add task
        print("2. View Tasks") # to view task 
        print("3. Mark Task Completed") # to mark task completed
        print("4. Delete Task") # to elete the task
        print("5. Exit") # to exit the application

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks updated. see you soon.")
            
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main() # the main program starts here 
