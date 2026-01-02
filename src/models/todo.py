"""
Todo model representing a single todo item.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with ID, title, status, and timestamps.
    """
    id: int
    title: str
    status: str = "pending"  # Can be "pending" or "complete"
    created_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    def __post_init__(self):
        """Initialize timestamps if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

        # Validate status
        if self.status not in ["pending", "complete"]:
            raise ValueError(f"Status must be 'pending' or 'complete', got '{self.status}'")

        # Validate title is not empty
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty or whitespace-only")

    def mark_complete(self) -> None:
        """Mark the todo as complete and set the completed_at timestamp."""
        self.status = "complete"
        self.completed_at = datetime.now()

    def mark_incomplete(self) -> None:
        """Mark the todo as incomplete and clear the completed_at timestamp."""
        self.status = "pending"
        self.completed_at = None

    def to_dict(self) -> dict:
        """Convert the todo to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }