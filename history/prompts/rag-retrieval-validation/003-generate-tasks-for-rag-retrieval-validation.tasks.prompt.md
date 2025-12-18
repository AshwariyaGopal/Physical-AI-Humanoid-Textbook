---
id: 003
title: Generate Tasks for RAG Retrieval Validation
stage: tasks
date: 2025-12-17
surface: agent
model: gemini-1.5-pro
feature: rag-retrieval-validation
branch: 001-rag-retrieval-validation
user: user
command: /sp.tasks
labels: [backend, rag, qdrant, cohere, tasks]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-rag-retrieval-validation/tasks.md
tests: null
---

## Prompt

description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.


## User Input

$ARGUMENTS

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

## Response snapshot

The `tasks.md` file has been generated.

**Summary:**
*   **Total task count**: 10
*   **Task count per user story**:
    *   Phase 1 (Setup): 0 tasks (reusing existing environment)
    *   Phase 2 (Foundational): 0 tasks (reusing existing client setups)
    *   User Story 1 (P1): 8 tasks
    *   Polish & Cross-Cutting Concerns: 2 tasks
*   **Parallel opportunities identified**: Limited due to tasks being within a single script and sequential dependencies, but initial setup and polish tasks offer some parallelism.
*   **Independent test criteria for each story**: Clearly stated in the `tasks.md` for User Story 1.
*   **Suggested MVP scope**: User Story 1.
*   **Format validation**: All tasks follow the checklist format (`- [ ] [TaskID] [P?] [Story?] Description with file path`).

## Outcome

- ✅ Impact: An actionable, dependency-ordered tasks list generated for the RAG retrieval validation feature.
- 🧪 Tests: No automated tests were run as this is a planning phase.
- 📁 Files: Generated `specs/001-rag-retrieval-validation/tasks.md`.
- 🔁 Next prompts: The user can now proceed with implementing the tasks listed in `tasks.md`.
- 🧠 Reflection: Successfully generated tasks based on the spec, plan, and data model. Appropriately identified reuse of existing environment and limited new setup tasks.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
