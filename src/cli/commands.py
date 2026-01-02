"""
CLI command handlers for the Console Todo Application.
"""
from src.services.todo_service import TodoService
from src.utils.validators import validate_todo_title, validate_todo_id
from src.utils.helpers import format_timestamp, format_status


class TodoCLI:
    """
    Command line interface for the todo application.
    """
    def __init__(self):
        """Initialize the CLI with a todo service."""
        self.service = TodoService()

    def handle_add(self, title: str):
        """
        Handle the add command.

        Args:
            title: The title of the todo to add
        """
        try:
            if not validate_todo_title(title):
                print("Error: Todo title cannot be empty")
                return

            todo = self.service.add_todo(title)
            print(f"Added todo with ID {todo.id}: {todo.title}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_list(self):
        """Handle the list command."""
        try:
            todos = self.service.list_todos()

            if not todos:
                print("No todos found")
                return

            print("ID | Status    | Title                    | Created At")
            print("---|-----------|--------------------------|------------------")
            for todo in todos:
                status = format_status(todo.status)
                created_at = format_timestamp(todo.created_at)
                title = todo.title[:24] + "..." if len(todo.title) > 24 else todo.title
                print(f"{todo.id:2} | {status:9} | {title:24} | {created_at}")
        except Exception as e:
            print(f"Error listing todos: {e}")

    def handle_update(self, todo_id: int, new_title: str):
        """
        Handle the update command.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo
        """
        try:
            if not validate_todo_id(todo_id):
                print(f"Error: Invalid todo ID {todo_id}")
                return

            if not validate_todo_title(new_title):
                print("Error: Todo title cannot be empty")
                return

            updated_todo = self.service.update_todo(todo_id, new_title)
            if updated_todo:
                print(f"Updated todo {todo_id}: {updated_todo.title}")
            else:
                print(f"Error: Todo with ID {todo_id} not found")
        except Exception as e:
            print(f"Error updating todo: {e}")

    def handle_delete(self, todo_id: int):
        """
        Handle the delete command.

        Args:
            todo_id: The ID of the todo to delete
        """
        try:
            if not validate_todo_id(todo_id):
                print(f"Error: Invalid todo ID {todo_id}")
                return

            success = self.service.delete_todo(todo_id)
            if success:
                print(f"Deleted todo with ID {todo_id}")
            else:
                print(f"Error: Todo with ID {todo_id} not found")
        except Exception as e:
            print(f"Error deleting todo: {e}")

    def handle_complete(self, todo_id: int):
        """
        Handle the complete command.

        Args:
            todo_id: The ID of the todo to mark complete
        """
        try:
            if not validate_todo_id(todo_id):
                print(f"Error: Invalid todo ID {todo_id}")
                return

            completed_todo = self.service.mark_complete(todo_id)
            if completed_todo:
                print(f"Marked todo {todo_id} as complete: {completed_todo.title}")
            else:
                print(f"Error: Todo with ID {todo_id} not found")
        except Exception as e:
            print(f"Error marking todo complete: {e}")