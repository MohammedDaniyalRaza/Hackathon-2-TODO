"""
Unit tests for the TodoService.
"""
import pytest
from src.services.todo_service import TodoService
from src.models.todo import Todo


class TestTodoService:
    """Tests for the TodoService."""

    def test_add_todo_with_valid_title(self):
        """Test adding a todo with a valid title."""
        service = TodoService()

        todo = service.add_todo("Test todo")

        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.status == "pending"
        assert len(service.todos) == 1
        assert service.todos[0] == todo

    def test_add_todo_with_empty_title_raises_error(self):
        """Test adding a todo with empty title raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Todo title cannot be empty"):
            service.add_todo("")

    def test_add_todo_with_whitespace_only_title_raises_error(self):
        """Test adding a todo with whitespace-only title raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Todo title cannot be empty"):
            service.add_todo("   ")

    def test_add_todo_assigns_unique_ids(self):
        """Test adding multiple todos assigns unique IDs."""
        service = TodoService()

        todo1 = service.add_todo("First todo")
        todo2 = service.add_todo("Second todo")
        todo3 = service.add_todo("Third todo")

        assert todo1.id == 1
        assert todo2.id == 2
        assert todo3.id == 3
        assert len(service.todos) == 3

    def test_list_todos_returns_all_todos(self):
        """Test listing todos returns all added todos."""
        service = TodoService()
        service.add_todo("First todo")
        service.add_todo("Second todo")

        todos = service.list_todos()

        assert len(todos) == 2
        assert todos[0].title == "First todo"
        assert todos[1].title == "Second todo"

    def test_list_todos_returns_empty_list_when_no_todos(self):
        """Test listing todos returns empty list when no todos exist."""
        service = TodoService()

        todos = service.list_todos()

        assert len(todos) == 0

    def test_get_todo_by_id_returns_correct_todo(self):
        """Test getting a todo by ID returns the correct todo."""
        service = TodoService()
        todo = service.add_todo("Test todo")
        expected_id = todo.id

        result = service.get_todo_by_id(expected_id)

        assert result is not None
        assert result.id == expected_id
        assert result.title == "Test todo"

    def test_get_todo_by_id_returns_none_for_invalid_id(self):
        """Test getting a todo by invalid ID returns None."""
        service = TodoService()
        service.add_todo("Test todo")

        result = service.get_todo_by_id(999)

        assert result is None

    def test_update_todo_updates_title(self):
        """Test updating a todo updates its title."""
        service = TodoService()
        original_todo = service.add_todo("Original title")
        original_id = original_todo.id

        updated_todo = service.update_todo(original_id, "Updated title")

        assert updated_todo is not None
        assert updated_todo.id == original_id
        assert updated_todo.title == "Updated title"
        assert service.todos[0].title == "Updated title"

    def test_update_todo_with_invalid_id_returns_none(self):
        """Test updating a todo with invalid ID returns None."""
        service = TodoService()
        service.add_todo("Test todo")

        result = service.update_todo(999, "Updated title")

        assert result is None

    def test_update_todo_with_empty_title_raises_error(self):
        """Test updating a todo with empty title raises ValueError."""
        service = TodoService()
        original_todo = service.add_todo("Original title")
        original_id = original_todo.id

        with pytest.raises(ValueError, match="Todo title cannot be empty"):
            service.update_todo(original_id, "")

    def test_delete_todo_removes_todo(self):
        """Test deleting a todo removes it from the list."""
        service = TodoService()
        todo = service.add_todo("Test todo")
        todo_id = todo.id

        result = service.delete_todo(todo_id)

        assert result is True
        assert len(service.todos) == 0

    def test_delete_todo_with_invalid_id_returns_false(self):
        """Test deleting a todo with invalid ID returns False."""
        service = TodoService()
        service.add_todo("Test todo")

        result = service.delete_todo(999)

        assert result is False
        assert len(service.todos) == 1

    def test_mark_complete_marks_todo_as_complete(self):
        """Test marking a todo as complete updates its status."""
        service = TodoService()
        todo = service.add_todo("Test todo")
        todo_id = todo.id

        result = service.mark_complete(todo_id)

        assert result is not None
        assert result.id == todo_id
        assert result.status == "complete"

    def test_mark_complete_with_invalid_id_returns_none(self):
        """Test marking a todo as complete with invalid ID returns None."""
        service = TodoService()
        service.add_todo("Test todo")

        result = service.mark_complete(999)

        assert result is None

    def test_mark_incomplete_marks_todo_as_incomplete(self):
        """Test marking a todo as incomplete updates its status."""
        service = TodoService()
        todo = service.add_todo("Test todo")
        todo_id = todo.id
        service.mark_complete(todo_id)  # Mark as complete first

        result = service.mark_incomplete(todo_id)

        assert result is not None
        assert result.id == todo_id
        assert result.status == "pending"