"""
Todo service handling business logic for todo operations.
"""
from typing import List, Optional
from datetime import datetime
from src.models.todo import Todo


class TodoService:
    """
    Service class handling all todo-related business logic with in-memory storage.
    """
    def __init__(self):
        """Initialize the service with empty storage."""
        self.todos: List[Todo] = []
        self.next_id = 1

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo with the given title.

        Args:
            title: The title of the todo

        Returns:
            The created Todo object
        """
        # Validate title
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty")

        # Create a new todo with unique ID
        todo = Todo(
            id=self.next_id,
            title=title.strip()
        )

        # Add to the list and increment next_id
        self.todos.append(todo)
        self.next_id += 1

        return todo

    def list_todos(self) -> List[Todo]:
        """
        Get all todos.

        Returns:
            List of all Todo objects
        """
        return self.todos

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: The ID of the todo

        Returns:
            The Todo object if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_title: str) -> Optional[Todo]:
        """
        Update the title of an existing todo.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            The updated Todo object if successful, None if todo not found
        """
        if not new_title or not new_title.strip():
            raise ValueError("Todo title cannot be empty")

        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.title = new_title.strip()
            return todo
        return None

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False

    def mark_complete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            The updated Todo object if successful, None if todo not found
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_complete()
            return todo
        return None

    def mark_incomplete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            The updated Todo object if successful, None if todo not found
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_incomplete()
            return todo
        return None