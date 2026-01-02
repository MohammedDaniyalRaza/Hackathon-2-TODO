---
description: "Task list for Console Todo Application implementation"
---

# Tasks: Console Todo Application

**Input**: Design documents from `specs/1-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure per implementation plan
- [X] T002 Create src directory and subdirectories (models, services, cli, utils)
- [X] T003 [P] Create tests directory and subdirectories (unit, integration)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Todo model in src/models/todo.py with id, title, status, timestamps
- [X] T005 Create TodoService in src/services/todo_service.py with in-memory storage
- [X] T006 Create CLI argument parser in src/app.py
- [X] T007 Create validators module in src/utils/validators.py
- [X] T008 Create helpers module in src/utils/helpers.py
- [X] T009 Create basic CLI command handlers in src/cli/commands.py
- [X] T010 Create README.md with project overview

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Items (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list from the command line interface

**Independent Test**: Can be fully tested by running the add command with various inputs and verifying the items appear in the list, delivering a functional todo creation capability.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T011 [P] [US1] Create Todo model tests in tests/unit/test_todo.py
- [X] T012 [P] [US1] Create TodoService add method tests in tests/unit/test_todo_service.py

### Implementation for User Story 1

- [X] T013 [US1] Implement Todo model with validation in src/models/todo.py
- [X] T014 [US1] Implement TodoService add_todo method in src/services/todo_service.py
- [X] T015 [US1] Implement add command handler in src/cli/commands.py
- [X] T016 [US1] Implement input validation for add command in src/utils/validators.py
- [X] T017 [US1] Update app.py to handle add command
- [X] T018 [US1] Test add functionality manually with various inputs

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Enable users to view all their todo items in a clear, readable format

**Independent Test**: Can be fully tested by adding items and then running the view command to verify all items are displayed correctly, delivering a complete visibility capability.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T019 [P] [US2] Create TodoService list method tests in tests/unit/test_todo_service.py
- [ ] T020 [US2] Create CLI list command tests in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T021 [US2] Implement TodoService list_todos method in src/services/todo_service.py
- [X] T022 [US2] Implement list command handler in src/cli/commands.py
- [X] T023 [US2] Update app.py to handle list command
- [X] T024 [US2] Test list functionality with empty and non-empty lists

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo Items (Priority: P2)

**Goal**: Enable users to modify the description of existing todo items by ID

**Independent Test**: Can be fully tested by updating items and verifying the changes persist, delivering a modification capability.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T025 [P] [US3] Create TodoService update method tests in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [X] T026 [US3] Implement TodoService update_todo method in src/services/todo_service.py
- [X] T027 [US3] Implement update command handler in src/cli/commands.py
- [X] T028 [US3] Update app.py to handle update command
- [X] T029 [US3] Test update functionality with valid and invalid IDs

**Checkpoint**: User Stories 1, 2, and 3 should now be independently functional

---

## Phase 6: User Story 4 - Delete Todo Items (Priority: P2)

**Goal**: Enable users to remove completed or unwanted todo items from their list by ID

**Independent Test**: Can be fully tested by deleting items and verifying they no longer appear in the list, delivering a cleanup capability.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T030 [P] [US4] Create TodoService delete method tests in tests/unit/test_todo_service.py

### Implementation for User Story 4

- [X] T031 [US4] Implement TodoService delete_todo method in src/services/todo_service.py
- [X] T032 [US4] Implement delete command handler in src/cli/commands.py
- [X] T033 [US4] Update app.py to handle delete command
- [X] T034 [US4] Test delete functionality with valid and invalid IDs

**Checkpoint**: User Stories 1, 2, 3, and 4 should now be independently functional

---

## Phase 7: User Story 5 - Mark Todo Items Complete (Priority: P2)

**Goal**: Enable users to mark todo items as completed to track their progress

**Independent Test**: Can be fully tested by marking items complete and verifying the status changes, delivering a progress tracking capability.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T035 [P] [US5] Create TodoService mark complete method tests in tests/unit/test_todo_service.py

### Implementation for User Story 5

- [X] T036 [US5] Implement TodoService mark_complete method in src/services/todo_service.py
- [X] T037 [US5] Implement complete command handler in src/cli/commands.py
- [X] T038 [US5] Update app.py to handle complete command
- [X] T039 [US5] Test mark complete functionality with valid and invalid IDs

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T040 [P] Add comprehensive error handling across all commands
- [X] T041 [P] Add type hints to all functions and methods
- [X] Add docstrings to all modules, classes, and functions (already present)
- [X] T043 [P] Create requirements.txt and pyproject.toml
- [X] T044 [P] Add documentation to README.md
- [ ] T045 Run full integration tests across all user stories
- [ ] T046 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Create Todo model tests in tests/unit/test_todo.py"
Task: "Create TodoService add method tests in tests/unit/test_todo_service.py"

# Launch all implementation for User Story 1 together:
Task: "Implement Todo model with validation in src/models/todo.py"
Task: "Implement TodoService add_todo method in src/services/todo_service.py"
Task: "Implement add command handler in src/cli/commands.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence