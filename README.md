# Task Tracker CLI

A command-line task management tool built in Python. Tasks are persisted locally to a JSON file, with full support for creation, updates, deletion, and status tracking across sessions.

## Features

- Add, update, and delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- Filter task listings by status
- Persistent JSON storage with automatic file initialisation
- Custom exception handling for invalid task operations

## Project Structure

```
task-tracker/
├── main.py     # Core TaskManager class and CLI entry point
├── exceptions.py       # Custom exception definitions
├── tasks.json          # Auto-generated task persistence file
└── test_main.py              # pytest test suite
```

## Getting Started

**Requirements**

- Python 3.x

**Installation**

```bash
git clone https://github.com/D3ssnk/task-tracker.git
cd task-tracker
```

**Running the application**

```bash
python main.py
```

## Usage

| Command | Description |
|---------|-------------|
| `add <description>` | Add a new task |
| `update <id> <description>` | Update an existing task's description |
| `delete <id>` | Delete a task by ID |
| `mark-todo <id>` | Mark a task as todo |
| `mark-in-progress <id>` | Mark a task as in-progress |
| `mark-done <id>` | Mark a task as done |
| `list` | List all tasks |
| `list <status>` | List tasks filtered by status |
| `help` | Display usage instructions |
| `exit` | Exit the application |

**Example session**

```
> add Buy groceries
task has been added

=========Tasks=========

id: 1
description: Buy groceries
status: todo

> mark-in-progress 1
task id: 1 has been marked as in-progress

> list in-progress

id: 1
description: Buy groceries
status: in-progress
```

## Running Tests

```bash
pytest test_main.py
```

## Technical Notes

- Task IDs are sequential and automatically reindexed after deletion to maintain contiguity
- The JSON storage file is initialised automatically on first run
- Invalid task IDs raise a custom `TaskNotFound` exception handled gracefully at the CLI layer