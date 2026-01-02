# Console Todo Application

A simple, in-memory command-line todo application built with Python.

## Features

- Add new todo items
- View all todo items
- Update existing todo items
- Delete todo items
- Mark todo items as complete

## Requirements

- Python 3.13+

## Installation

No installation required. Simply run the application with Python.

## Usage

```bash
# Add a new todo
python src/app.py add "Buy groceries"

# List all todos
python src/app.py list

# Update a todo
python src/app.py update 1 "Buy groceries and cook dinner"

# Delete a todo
python src/app.py delete 1

# Mark a todo as complete
python src/app.py complete 1
```

## Architecture

This application follows a layered architecture:

- **Models**: Data structures (Todo entity)
- **Services**: Business logic (TodoService)
- **CLI**: Command line interface (commands and menu)
- **Utils**: Helper functions and validators

All data is stored in-memory only and will be lost when the application exits.

## Project Structure

```
src/
├── models/
│   └── todo.py          # Todo entity (id, title, status, timestamps)
├── services/
│   └── todo_service.py  # Business logic (CRUD, mark complete)
├── cli/
│   ├── commands.py      # CLI command handlers
│   └── menu.py          # User input & routing
├── utils/
│   ├── validators.py    # Input validation
│   └── helpers.py       # Shared utilities
└── app.py               # Application entry point

tests/
├── unit/
│   ├── test_todo.py     # Todo model tests
│   └── test_todo_service.py  # Service logic tests
└── integration/
    └── test_cli.py      # CLI integration tests
```

## Running Tests

To run the unit tests:

```bash
pip install pytest
pytest tests/unit/
```

## Design Principles

- **In-Memory Only**: All data is stored in memory and resets on application restart
- **Clean Architecture**: Clear separation between data models, business logic, and user interface
- **Type Safety**: Full type hinting throughout the codebase
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Validation**: Input validation at all levels to ensure data integrity