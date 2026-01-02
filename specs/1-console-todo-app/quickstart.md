# Quickstart Guide: Console Todo Application

## Prerequisites
- Python 3.13 or higher
- Basic command line knowledge

## Installation
1. Clone the repository (or create the project structure)
2. Ensure Python 3.13+ is installed
3. No additional dependencies required (uses built-in libraries only)

## Running the Application
```bash
python src/app.py --help
```

## Basic Usage
### Add a new todo
```bash
python src/app.py add "Buy groceries"
```

### List all todos
```bash
python src/app.py list
```

### Update a todo
```bash
python src/app.py update 1 "Buy groceries and cook dinner"
```

### Mark a todo as complete
```bash
python src/app.py complete 1
```

### Delete a todo
```bash
python src/app.py delete 1
```

## Example Workflow
1. Add todos: `python src/app.py add "Complete project proposal"`
2. View todos: `python src/app.py list`
3. Mark complete: `python src/app.py complete 1`
4. Add more todos: `python src/app.py add "Review code"`
5. List all: `python src/app.py list`

## Expected Output
- Success operations return confirmation messages
- Error operations return descriptive error messages
- List command shows all todos with their status and ID