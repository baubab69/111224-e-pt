from pathlib import Path
import json
import os
from task import Task



class Manager:
    

    def __init__(self, config_file_name: str):
        path = Path(config_file_name)
        self.task_list = []
        self.task_list_file = None

        try:
            with open(path, 'r', encoding="utf-8") as config_file:
                lines = config_file.readlines()
                for line in lines:
                    if line.startswith('task_list_file'):
                        self.task_list_file = line.split(':')[1].strip().replace("'", "").replace('"', '')
                        if os.path.isfile(self.task_list_file):
                            self.__load_task_list()
        except FileNotFoundError:
            print(f"Configuration file {config_file_name} not found.")
        except Exception as e:
            print(f"An error occurred while reading the configuration file: {e}")

    def __load_task_list(self):
       
        if self.task_list_file and os.path.isfile(self.task_list_file):
            try:
                with open(self.task_list_file, 'r', encoding="utf-8") as file:
                    tasks = json.load(file)
                    self.task_list = [Task.from_dict(task) for task in tasks]
            except FileNotFoundError:
                self.task_list = []
            except json.decoder.JSONDecodeError:
                print("Error: The task list file is not a valid JSON.")
                self.task_list = []
        else:
            print("No task list file specified in the config.")

    def save_task_list(self):
      
        if not self.task_list_file:
            print("No task list file specified in the config.")
            return
        with open(self.task_list_file, 'w', encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.task_list], file, ensure_ascii=False, indent=4)

    def create_task(self, title: str):
      
        if any(task.title == title for task in self.task_list):
            print(f"Task with title '{title}' already exists.")
            return None

        task = Task(title)
        task.id = len(self.task_list) + 1  # Assigning unique ID
        self.task_list.append(task)
        self.save_task_list()
        return task

    def delete_task(self, task_id: int):
       
        for task in self.task_list:
            if task.id == task_id:
                self.task_list.remove(task)
                self.save_task_list()
                print(f"Task with id {task_id} has been deleted.")
                return
        print(f"Task with id {task_id} not found.")

    def get_task_list(self):
    
        return self.task_list



if __name__ == "__main__":
    manager = Manager("config.yaml")

    while True:
        print("\nTask Tracker Menu:")
        print("1. Show task list")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            tasks = manager.get_task_list()
            if tasks:
                print("\nTask List:")
                for task in tasks:
                    print(f"id - {task.id}: {task.title} (Status: {task.status})")
            else:
                print("\nNo tasks found.")

        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                manager.create_task(title)
                print(f"Task '{title}' added successfully!")
            else:
                print("Task title cannot be empty.")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == "4":
            print("Saving tasks and exiting...")
            manager.save_task_list()
            break

        else:
            print("Invalid choice, please try again.")
