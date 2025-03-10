import pytest
from datetime import datetime
from task import Task

def test_title_setter_with_valid_string():
    task = Task("Initial Title")
    task.title = "New Title"
    assert task.title == "New Title"

def test_title_setter_with_empty_string():
    task = Task("Initial Title")
    task.title = ""
    assert task.title == "Initial Title"

def test_description_setter_with_valid_string():
    task = Task("Initial Title")
    task.description = "New Description"
    assert task.description == "New Description"

def test_description_setter_with_non_string():
    task = Task("Initial Title")
    task.description = 123
    assert task.description is None

def test_deadline_setter_with_valid_datetime():
    task = Task("Initial Title")
    new_deadline = datetime(2023, 12, 31)
    task.deadline = new_deadline
    assert task.deadline == new_deadline

def test_deadline_setter_with_non_datetime():
    task = Task("Initial Title")
    task.deadline = "2023-12-31"
    assert task.deadline is None

def test_status_setter_with_valid_string():
    task = Task("Initial Title")
    task.status = "Completed"
    assert task.status == "Completed"

def test_id_setter_with_valid_integer():
    task = Task("Initial Title")
    task.id = 1
    assert task.id == 1