import json
import os
from pathlib import Path

from task import Task


class Manager:
    last_id = 0
    def __init__(self, config_file_name: str):
        """
        Manager constructor
        :param config_file_name:
        """
        path = Path(config_file_name)
        self.task_list = []
        if path.exists():
            with open(path) as config_file:
                lines = config_file.readlines()
                for line in lines:
                    if line.startswith('task_list_file'):
                        self.task_list_file = line.split(':')[1].strip().replace("'", "").replace('"', '')
                        if os.path.isfile(self.task_list_file):
                            self.__load_task_list(self.task_list_file)
                            self.last_id = len(self.task_list) + 1


    @staticmethod
    def __load_task_list(task_list_file: str) -> list[Task]:
        """
        Load task list from file
        :param task_list_file:
        :return:
        """
        try:
            with open (task_list_file) as file:
                task_list = [Task.from_json(el) for el in json.load(file)]
        except FileNotFoundError:
            task_list = []
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON, creating empty task list")
            task_list = []
        return task_list

    def save_task_list(self):
        """
        Save task list to file
        :return:
        """
        with open(self.task_list_file, 'w') as file:
            json.dump([task.to_dict() for task in self.task_list], file)


    def create_task(self, title: str) -> Task:
        """
        Create new task
        :param title:
        :return:
        """
        task = Task(title)
        task.id = self.last_id
        self.last_id += 1
        self.task_list.append(task)
        return task

    def delete_task(self, task_id: int):
        """
        Delete task by id
        :param task_id:
        :return:
        """
        for task in self.task_list:
            if task.id == task_id:
                self.task_list.remove(task)
                break
        else:
            print(f"Task with id {task_id} not found")

    def get_task_list(self):
        """
        Get task list
        :return:
        """
        return self.task_list
#
# m = Manager('config.yaml')
# print(m.task_list_file)
# print(m.create_task('Test task'))
# print(m.get_task_list())
# print(m.create_task('Test task 2'))
# print(m.get_task_list())
# print(m.delete_task(1))
# print(m.get_task_list())
# print(m.save_task_list())
# print(m.get_task_list())
