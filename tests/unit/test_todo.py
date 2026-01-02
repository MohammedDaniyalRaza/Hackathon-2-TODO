"""
Unit tests for the Todo model.
"""
import pytest
from datetime import datetime
from src.models.todo import Todo


class TestTodo:
    """Tests for the Todo model."""

    def test_create_todo_with_valid_data(self):
        """Test creating a todo with valid data."""
        todo = Todo(id=1, title="Test todo")

        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.status == "pending"
        assert todo.created_at is not None
        assert todo.completed_at is None

    def test_create_todo_with_status_complete(self):
        """Test creating a todo with complete status."""
        todo = Todo(id=1, title="Test todo", status="complete")

        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.status == "complete"
        assert todo.created_at is not None
        assert todo.completed_at is None

    def test_create_todo_fails_with_empty_title(self):
        """Test creating a todo fails with empty title."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Todo(id=1, title="")

    def test_create_todo_fails_with_whitespace_only_title(self):
        """Test creating a todo fails with whitespace-only title."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Todo(id=1, title="   ")

    def test_create_todo_fails_with_invalid_status(self):
        """Test creating a todo fails with invalid status."""
        with pytest.raises(ValueError, match="Status must be"):
            Todo(id=1, title="Test todo", status="invalid")

    def test_mark_complete_sets_status_and_timestamp(self):
        """Test marking a todo as complete updates status and timestamp."""
        todo = Todo(id=1, title="Test todo")

        # Initially pending
        assert todo.status == "pending"
        assert todo.completed_at is None

        # Mark complete
        todo.mark_complete()

        assert todo.status == "complete"
        assert todo.completed_at is not None

    def test_mark_incomplete_sets_status_and_clears_timestamp(self):
        """Test marking a todo as incomplete updates status and clears timestamp."""
        todo = Todo(id=1, title="Test todo", status="complete")
        todo.mark_complete()  # Set to complete first

        # Initially complete
        assert todo.status == "complete"
        assert todo.completed_at is not None

        # Mark incomplete
        todo.mark_incomplete()

        assert todo.status == "pending"
        assert todo.completed_at is None

    def test_to_dict_returns_correct_format(self):
        """Test converting todo to dictionary returns correct format."""
        created_at = datetime(2023, 1, 1, 12, 0, 0)
        todo = Todo(id=1, title="Test todo", created_at=created_at)

        result = todo.to_dict()

        expected = {
            "id": 1,
            "title": "Test todo",
            "status": "pending",
            "created_at": "2023-01-01T12:00:00",
            "completed_at": None
        }

        assert result == expected