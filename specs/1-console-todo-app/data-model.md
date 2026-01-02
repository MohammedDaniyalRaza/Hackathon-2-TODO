# Data Model: Console Todo Application

## Todo Entity

### Fields
- **id**: Integer (auto-generated, unique identifier)
- **title**: String (required, the todo description)
- **status**: String (enum: "pending", "complete")
- **created_at**: DateTime (timestamp when todo was created)
- **completed_at**: DateTime (optional, timestamp when todo was marked complete)

### Validation Rules
- Title must not be empty or whitespace-only
- ID must be unique within the application session
- Status must be one of the allowed values ("pending", "complete")
- created_at must be set when the todo is created
- completed_at can only be set when status is "complete"

### State Transitions
- Initial state: status = "pending", completed_at = null
- When marked complete: status changes to "complete", completed_at set to current time
- When marked incomplete: status changes to "pending", completed_at set to null

## In-Memory Storage Structure
- **todos**: List of Todo entities
- **next_id**: Integer (auto-incrementing counter for ID generation)