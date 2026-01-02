"""
Main application entry point for the Console Todo Application.
"""
import argparse
import sys
import os
import importlib.util

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.cli.commands import TodoCLI


def main():
    """
    Main entry point for the todo application.
    """
    cli = TodoCLI()

    parser = argparse.ArgumentParser(
        description="Console Todo Application - Manage your tasks from the command line"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo")
    add_parser.add_argument("title", nargs="*", help="Title of the todo")

    # List command
    list_parser = subparsers.add_parser("list", help="List all todos")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a todo")
    update_parser.add_argument("id", type=int, help="ID of the todo to update")
    update_parser.add_argument("title", nargs="*", help="New title for the todo")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_parser.add_argument("id", type=int, help="ID of the todo to delete")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a todo as complete")
    complete_parser.add_argument("id", type=int, help="ID of the todo to complete")

    # Parse arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "add":
        title = " ".join(args.title) if args.title else ""
        cli.handle_add(title)
    elif args.command == "list":
        cli.handle_list()
    elif args.command == "update":
        title = " ".join(args.title) if args.title else ""
        cli.handle_update(args.id, title)
    elif args.command == "delete":
        cli.handle_delete(args.id)
    elif args.command == "complete":
        cli.handle_complete(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()