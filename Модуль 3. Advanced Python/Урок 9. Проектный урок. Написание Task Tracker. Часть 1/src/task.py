from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """
    This class represents a task for task management system
    """

    def __init__(self, title: str):
        """
        Task constructor
        :param title:
        """

    @property
    def title(self):
        """
        Get task title
        :return:
        """

    @title.setter
    def title(self, title):
        """
        Set task title
        :param title:
        :return:
        """

    @property
    def description(self):
        """
        Get task description
        :return:
        """

    @description.setter
    def description(self, description):
        """
        Set task description
        :param description:
        :return:
        """

    @property
    def deadline(self):
        """
        Get task deadline
        :return:
        """

    @deadline.setter
    def deadline(self, deadline: datetime):
        """
        Set task deadline
        :param deadline:
        :return:
        """

    @property
    def status(self):
        """
        Get task status
        :return:
        """

    @status.setter
    def status(self, new_status: str):
        """
        Set task status
        :param new_status:
        :return:
        """

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id: int):
        """
        Set task id
        :param new_id:
        :return:
        """
