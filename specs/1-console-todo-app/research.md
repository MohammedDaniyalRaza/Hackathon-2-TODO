# Research: Console Todo Application

## Decision: Python Console Application Architecture
**Rationale**: Following the layered architecture approach with clear separation of concerns as specified in the requirements. This provides modularity and testability while keeping the implementation simple for Phase I.

## Decision: In-Memory Data Storage
**Rationale**: As specified in requirements, using in-memory storage (Python lists/dicts) to maintain state only during application runtime. This meets the constraint of no external persistence while providing necessary functionality.

## Decision: CLI Framework
**Rationale**: Using Python's built-in argparse module for command-line parsing rather than external dependencies. This keeps the application lightweight and follows the constraint of using only built-in libraries where possible.

## Decision: Data Model Design
**Rationale**: Todo entity will include ID, title, status, and timestamps as specified. Using a simple class structure with appropriate methods for state management.

## Decision: Testing Framework
**Rationale**: Using pytest for unit tests as it's the most common and well-supported testing framework for Python applications. This meets the constitution requirement for testability.

## Decision: Project Structure
**Rationale**: Following the specified layered architecture with models, services, cli, and utils packages. This provides clear separation of concerns and makes the codebase maintainable and extensible.