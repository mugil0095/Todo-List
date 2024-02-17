import os

class TodoManager:
    def __init__(self):
        self.tasks_file = "data/tasks.txt"

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_completed()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("\nTodo List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

    def add_task(self):
        task = input("Enter task: ")
        with open(self.tasks_file, "a") as f:
            f.write(task + "\n")
        print("Task added successfully.")

    def view_tasks(self):
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, "r") as f:
                tasks = f.readlines()
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")

    def mark_completed(self):
        self.view_tasks()
        task_number = int(input("Enter task number to mark as completed: ")) - 1
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, "r") as f:
                tasks = f.readlines()
            if 0 <= task_number < len(tasks):
                tasks[task_number] = tasks[task_number].strip() + " (Completed)\n"
                with open(self.tasks_file, "w") as f:
                    f.writelines(tasks)
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks found.")
