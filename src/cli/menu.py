"""
Interactive menu system for the Console Todo Application.
"""
from typing import Optional
from src.services.todo_service import TodoService
from src.utils.validators import validate_todo_title, validate_todo_id


class TodoMenu:
    """
    Interactive menu system for the todo application with continuous loop.
    """
    def __init__(self):
        """Initialize the menu with a todo service."""
        self.service = TodoService()

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*40)
        print("         TODO APPLICATION MENU")
        print("="*40)
        print("1. Add Todo")
        print("2. View All Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Mark Todo Complete")
        print("6. Mark Todo Incomplete")
        print("7. Exit")
        print("="*40)

    def get_user_choice(self) -> str:
        """Get and validate user choice from the menu."""
        while True:
            try:
                choice = input("Enter your choice (1-7): ").strip()
                if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except KeyboardInterrupt:
                print("\n\nExiting application...")
                return "7"  # Return exit option if interrupted

    def handle_add_todo(self):
        """Handle adding a new todo."""
        print("\n--- ADD TODO ---")
        title = input("Enter todo title: ").strip()

        if not validate_todo_title(title):
            print("Error: Todo title cannot be empty or whitespace-only.")
            return

        try:
            todo = self.service.add_todo(title)
            print(f"✓ Added todo with ID {todo.id}: {todo.title}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view_todos(self):
        """Handle viewing all todos."""
        print("\n--- ALL TODOS ---")
        todos = self.service.list_todos()

        if not todos:
            print("No todos found.")
            return

        print(f"{'ID':<3} | {'Status':<10} | {'Title':<30}")
        print("-" * 47)
        for todo in todos:
            status = todo.status.upper()
            title = todo.title[:27] + "..." if len(todo.title) > 27 else todo.title
            print(f"{todo.id:<3} | {status:<10} | {title:<30}")

    def handle_update_todo(self):
        """Handle updating a todo."""
        print("\n--- UPDATE TODO ---")
        if not self.service.list_todos():
            print("No todos available to update.")
            return

        self.handle_view_todos()
        id_input = input("Enter the ID of the todo to update: ").strip()

        if not validate_todo_id(id_input):
            print("Error: Please enter a valid positive integer ID.")
            return

        todo_id = int(id_input)
        todo = self.service.get_todo_by_id(todo_id)

        if not todo:
            print(f"Error: Todo with ID {todo_id} not found.")
            return

        new_title = input(f"Enter new title for todo '{todo.title}': ").strip()

        if not validate_todo_title(new_title):
            print("Error: Todo title cannot be empty or whitespace-only.")
            return

        try:
            updated_todo = self.service.update_todo(todo_id, new_title)
            if updated_todo:
                print(f"✓ Updated todo {todo_id}: {updated_todo.title}")
            else:
                print(f"Error: Failed to update todo with ID {todo_id}.")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_delete_todo(self):
        """Handle deleting a todo."""
        print("\n--- DELETE TODO ---")
        if not self.service.list_todos():
            print("No todos available to delete.")
            return

        self.handle_view_todos()
        id_input = input("Enter the ID of the todo to delete: ").strip()

        if not validate_todo_id(id_input):
            print("Error: Please enter a valid positive integer ID.")
            return

        todo_id = int(id_input)
        todo = self.service.get_todo_by_id(todo_id)

        if not todo:
            print(f"Error: Todo with ID {todo_id} not found.")
            return

        confirmation = input(f"Are you sure you want to delete '{todo.title}'? (y/N): ").strip().lower()
        if confirmation in ['y', 'yes']:
            success = self.service.delete_todo(todo_id)
            if success:
                print(f"✓ Deleted todo with ID {todo_id}")
            else:
                print(f"Error: Failed to delete todo with ID {todo_id}.")
        else:
            print("Deletion cancelled.")

    def handle_mark_complete(self):
        """Handle marking a todo as complete."""
        print("\n--- MARK TODO COMPLETE ---")
        if not self.service.list_todos():
            print("No todos available to mark complete.")
            return

        # Show only pending todos
        all_todos = self.service.list_todos()
        pending_todos = [todo for todo in all_todos if todo.status == "pending"]

        if not pending_todos:
            print("No pending todos to mark complete.")
            return

        print(f"{'ID':<3} | {'Status':<10} | {'Title':<30}")
        print("-" * 47)
        for todo in pending_todos:
            title = todo.title[:27] + "..." if len(todo.title) > 27 else todo.title
            print(f"{todo.id:<3} | {'PENDING':<10} | {title:<30}")

        id_input = input("Enter the ID of the todo to mark complete: ").strip()

        if not validate_todo_id(id_input):
            print("Error: Please enter a valid positive integer ID.")
            return

        todo_id = int(id_input)
        todo = self.service.get_todo_by_id(todo_id)

        if not todo:
            print(f"Error: Todo with ID {todo_id} not found.")
            return

        if todo.status == "complete":
            print(f"Todo with ID {todo_id} is already marked as complete.")
            return

        updated_todo = self.service.mark_complete(todo_id)
        if updated_todo:
            print(f"✓ Marked todo {todo_id} as complete: {updated_todo.title}")
        else:
            print(f"Error: Failed to mark todo with ID {todo_id} as complete.")

    def handle_mark_incomplete(self):
        """Handle marking a todo as incomplete."""
        print("\n--- MARK TODO INCOMPLETE ---")
        if not self.service.list_todos():
            print("No todos available to mark incomplete.")
            return

        # Show only completed todos
        all_todos = self.service.list_todos()
        completed_todos = [todo for todo in all_todos if todo.status == "complete"]

        if not completed_todos:
            print("No completed todos to mark incomplete.")
            return

        print(f"{'ID':<3} | {'Status':<10} | {'Title':<30}")
        print("-" * 47)
        for todo in completed_todos:
            title = todo.title[:27] + "..." if len(todo.title) > 27 else todo.title
            print(f"{todo.id:<3} | {'COMPLETE':<10} | {title:<30}")

        id_input = input("Enter the ID of the todo to mark incomplete: ").strip()

        if not validate_todo_id(id_input):
            print("Error: Please enter a valid positive integer ID.")
            return

        todo_id = int(id_input)
        todo = self.service.get_todo_by_id(todo_id)

        if not todo:
            print(f"Error: Todo with ID {todo_id} not found.")
            return

        if todo.status == "pending":
            print(f"Todo with ID {todo_id} is already marked as pending.")
            return

        updated_todo = self.service.mark_incomplete(todo_id)
        if updated_todo:
            print(f"✓ Marked todo {todo_id} as incomplete: {updated_todo.title}")
        else:
            print(f"Error: Failed to mark todo with ID {todo_id} as incomplete.")

    def run(self):
        """Run the interactive menu loop until user chooses to exit."""
        print("Welcome to the Todo Application!")
        print("This is a session-based console application.")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.handle_add_todo()
            elif choice == "2":
                self.handle_view_todos()
            elif choice == "3":
                self.handle_update_todo()
            elif choice == "4":
                self.handle_delete_todo()
            elif choice == "5":
                self.handle_mark_complete()
            elif choice == "6":
                self.handle_mark_incomplete()
            elif choice == "7":
                print("\nThank you for using the Todo Application. Goodbye!")
                break

            # Pause to let user see the result before showing menu again
            input("\nPress Enter to continue...")