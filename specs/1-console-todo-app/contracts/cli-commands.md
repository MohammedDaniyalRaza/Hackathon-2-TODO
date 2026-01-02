# CLI Command Contracts: Console Todo Application

## Command Interface Specification

### Add Todo Command
- **Command**: `todo add <title>`
- **Input**: Todo title (string)
- **Output**: Success message with assigned ID
- **Error cases**:
  - Empty title → "Error: Todo title cannot be empty"
  - Invalid input → "Error: Invalid input format"

### List Todos Command
- **Command**: `todo list`
- **Input**: None
- **Output**: Formatted list of all todos with ID, title, and status
- **Error cases**:
  - No todos → "No todos found"

### Update Todo Command
- **Command**: `todo update <id> <new_title>`
- **Input**: Todo ID (integer), new title (string)
- **Output**: Success message
- **Error cases**:
  - Invalid ID → "Error: Todo with ID <id> not found"
  - Empty new title → "Error: Todo title cannot be empty"

### Delete Todo Command
- **Command**: `todo delete <id>`
- **Input**: Todo ID (integer)
- **Output**: Success message
- **Error cases**:
  - Invalid ID → "Error: Todo with ID <id> not found"

### Complete Todo Command
- **Command**: `todo complete <id>`
- **Input**: Todo ID (integer)
- **Output**: Success message
- **Error cases**:
  - Invalid ID → "Error: Todo with ID <id> not found"

## Data Format Contracts

### Todo Representation
```
{
  "id": integer,
  "title": string,
  "status": "pending" | "complete",
  "created_at": ISO8601 datetime string,
  "completed_at": ISO8601 datetime string | null
}
```

### Success Response
```
{
  "status": "success",
  "message": string,
  "data": object | null
}
```

### Error Response
```
{
  "status": "error",
  "message": string
}
```