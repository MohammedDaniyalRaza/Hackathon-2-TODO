# Session-Based Console Todo Application

A simple, interactive command-line todo application built with Python that runs in a continuous session until the user chooses to exit.

## Features

- Interactive menu system with continuous loop
- Add new todo items
- View all todo items
- Update existing todo items
- Delete todo items
- Mark todo items as complete
- Mark todo items as incomplete
- Exit option

## Requirements

- Python 3.13+

## Installation

No installation required. Simply run the application with Python.

## Usage

```bash
python main.py
```

The application will start an interactive session with a menu. Follow the prompts to manage your todos. The session continues until you choose the Exit option.

## Architecture

This application follows a layered architecture:

- **Models**: Data structures (Todo entity in `src/models/todo.py`)
- **Services**: Business logic (TodoService in `src/services/todo_service.py`)
- **CLI**: Interactive menu system (TodoMenu in `src/cli/menu.py`)
- **Utils**: Helper functions and validators (`src/utils/`)

All data is stored in-memory only and will be lost when the application exits.

## Project Structure

```
src/
├── models/
│   └── todo.py          # Todo entity (id, title, status, timestamps)
├── services/
│   └── todo_service.py  # Business logic (CRUD, mark complete/incomplete)
├── cli/
│   └── menu.py          # Interactive menu system
└── utils/
    └── validators.py    # Input validation

main.py                  # Application entry point
```

## Design Principles

- **Session-Based**: Continuous interactive loop until user chooses Exit
- **In-Memory Only**: All data is stored in memory and resets on application restart
- **Clean Architecture**: Clear separation between data models, business logic, and user interface
- **Type Safety**: Full type hinting throughout the codebase
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Validation**: Input validation at all levels to ensure data integrity