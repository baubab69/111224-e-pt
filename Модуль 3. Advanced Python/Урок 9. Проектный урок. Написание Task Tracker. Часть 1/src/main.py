from manager import Manager
from task import Task


def get_help_info(command_list: dict):
    """
    Prints the main menu and available commands.

    Args:
        command_list (dict): A dictionary of commands and their descriptions.
    """
    return 'get_task_list', 'check_config'

def get_task_list(manager: Manager):
    """
    Prints the list of tasks managed by the given manager.
    
    Args:
        manager (Manager): The manager instance to retrieve the task list from.
    """
    return manager.get_task_list()
    

def check_config():
    """
    Checks if the configuration file 'config.yaml' exists.
    If it does not exist, creates an empty 'config.yaml' file.
    """

def main():
    """
    The main function that runs the task manager application.
    It initializes the manager, displays the main menu, and processes user commands.
    """

if __name__ == '__main__':
    main()