#!/usr/bin/env python3
"""
Main entry point for the Session-Based Console Todo Application.
"""
from src.cli.menu import TodoMenu


def main():
    """
    Main function to run the interactive todo application.
    """
    menu = TodoMenu()
    menu.run()


if __name__ == "__main__":
    main()