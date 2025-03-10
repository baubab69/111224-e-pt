import pytest
from unittest.mock import patch, mock_open, MagicMock
from manager import Manager
from task import Task

@patch('builtins.open', new_callable=mock_open, read_data="task_list_file: 'task_list.pkl'")
@patch('os.path.isfile', return_value=True)
@patch('pickle.load', return_value=[])
def test_initialization_with_existing_task_list_file(mock_pickle_load, mock_isfile, mock_open):
    manager = Manager('config.yaml')
    assert manager.get_task_list() == []

@patch('builtins.open', new_callable=mock_open, read_data="task_list_file: 'task_list.pkl'")
@patch('os.path.isfile', return_value=False)
def test_initialization_with_non_existing_task_list_file(mock_isfile, mock_open):
    manager = Manager('config.yaml')
    assert manager.get_task_list() == []

@patch('builtins.open', new_callable=mock_open, read_data="task_list_file: 'task_list.pkl'")
@patch('pickle.dump')
def test_save_task_list(mock_pickle_dump, mock_open):
    manager = Manager('config.yaml')
    manager.save_task_list()
    mock_pickle_dump.assert_called_once()

@patch('builtins.open', new_callable=mock_open, read_data="task_list_file: 'task_list.pkl'")
def test_create_task(mock_open):
    manager = Manager('config.yaml')
    manager.create_task('New Task')
    assert len(manager.get_task_list()) == 1
    assert manager.get_task_list()[0].title == 'New Task'

@patch('builtins.open', new_callable=mock_open, read_data="task_list_file: 'task_list.pkl'")
def test_delete_existing_task(mock_open):
    manager = Manager('config.yaml')
    manager.create_task('Task to Delete')
    task_id = manager.get_task_list()[0].id
    manager.delete_task(task_id)
    assert len(manager.get_task_list()) == 0

@patch('builtins.open', new_callable=mock_open, read_data="task_list_file: 'task_list.pkl'")
def test_delete_non_existing_task(mock_open):
    manager = Manager('config.yaml')
    manager.create_task('Task to Delete')
    manager.delete_task(999)
    assert len(manager.get_task_list()) == 1