from main import TaskManager
import json
import pytest
import os

@pytest.fixture
def test_json_file():
    if not os.path.exists("test_json.json"):
        with open("test_json.json","w") as file:
            file.write('[]')
    yield "test_json.json"
    if os.path.exists("test_json.json"):
        os.remove("test_json.json")
    

@pytest.fixture
def test_task_manager(test_json_file):
    return TaskManager(test_json_file)

def test_add(test_task_manager, test_json_file):
    tmp_tasks = [{'id': 1, 'description': 'Make Coffee'}]
    test_task_manager.add("Make Coffee")

    with open(test_json_file, "r") as file:
        file_data = json.load(file)

    assert file_data == tmp_tasks, "Correctly adds task with ID as one"

    test_task_manager.add("Make Tea")
    tmp_tasks.append({'id': 2, 'description': 'Make Tea'})

    assert file_data == tmp_tasks, "Correctly adds task with incremented ID"