from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """
    This class represents a task for task management system
    """

    def __init__(self, title: str ):
        """
        Task constructor
        :param title:
        """
        self.__title = title
        self.__description = None
        self.__deadline = None
        self.__id = None



    @property
    def title(self):
        """
        Get task title
        :return:
        """
        return self.__title

    @title.setter
    def title(self, title):
        """
        Set task title
        :param title:
        :return:
        """
        if isinstance(title, str) and title != '':
            self.__title = title
            return self.__title

    @property
    def description(self):
        """
        Get task description
        :return:
        """
        return self.__description


    @description.setter
    def description(self, description):
        """
        Set task description
        :param description:
        :return:
        """
        if not isinstance(description, str):
            return self.__description
        self.__description = description
        return self.__description

    @property
    def deadline(self):
        """
        Get task deadline
        :return:
        """
        return self.__deadline
    @deadline.setter
    def deadline(self, deadline: datetime):
        """
        Set task deadline
        :param deadline:
        :return:
        """
        if isinstance(deadline, datetime):
            self.__deadline = deadline
            return self.__deadline


    @property
    def status(self):
        """
        Get task status
        :return:
        """
        return self.__new_status

    @status.setter
    def status(self, new_status: str):
        """
        Set task status
        :param new_status:
        :return:
        """
        if isinstance(new_status, str):
            self.__new_status = new_status
            return self.__new_status
        raise ValueError('Неправильное занчение!')

    @property
    def id(self):
        """
        Get task id
        :return:
        """
        return self.__id

    @id.setter
    def id(self, new_id: int):
        """
        Set task id
        :param new_id:
        :return:
        """
        if isinstance(new_id, int):
            self.__new_id = new_id
            return self.__new_id

    def to_dict(self):
        """
        Convert task to dictionary
        :return:
        """
        return {
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline,
            'id': self.id
        }

    def __str__(self):
        """
        Convert task to string
        :return:
        """
        return f"Task({self.title}, {self.description}, {self.deadline}, {self.id})"

    @classmethod
    def from_json(cls, data: dict):
        """
        Convert json to task
        :param data:
        :return:
        """
        task = cls(data.get('title'))
        task = data.get('description')
        task = data.get('deadline')
        task = data.get('id')