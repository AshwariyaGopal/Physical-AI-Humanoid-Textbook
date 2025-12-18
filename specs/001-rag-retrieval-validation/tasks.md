---

description: "Task list for Retrieval and validation of embedded textbook content for RAG readiness"
---

# Tasks: Retrieval and validation of embedded textbook content for RAG readiness

**Input**: Design documents from `specs/001-rag-retrieval-validation/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Note**: The existing `backend/` directory from Spec-1 (embedding pipeline) will be reused, including its Python virtual environment (`.venv`), `requirements.txt`, and `.env.example`.

**Tests**: No specific test tasks are requested in the feature specification, but the output of the script will serve as a direct validation mechanism.

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

No new setup tasks are required for this feature, as it leverages the existing `backend/` environment established in Spec-1.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

No new foundational tasks are strictly required for this feature, as it directly reuses the existing Cohere and Qdrant client setup logic within its script.

---

## Phase 3: User Story 1 - Retrieval and Validation (Priority: P1) 🎯 MVP

**Goal**: As a developer, I want to retrieve stored embeddings from Qdrant and validate that the RAG retrieval pipeline returns correct, relevant textbook chunks for user queries, so that I can trust the retrieval quality.

**Independent Test**: Can be fully tested by providing a query, performing a vector similarity search in Qdrant, and checking if the retrieved chunks are semantically relevant and include correct metadata.

### Implementation for User Story 1 (Script: `backend/retrieve.py`)

- [x] T001 [US1] Create `backend/retrieve.py` script.
- [x] T002 [US1] Load environment variables (`COHERE_API_KEY`, `QDRANT_API_KEY`, `QDRANT_URL`) from `.env` in `backend/retrieve.py`.
- [x] T003 [US1] Initialize Cohere client in `backend/retrieve.py`.
- [x] T004 [US1] Initialize Qdrant client, connecting to `rag_embedding` collection in `backend/retrieve.py`.
- [x] T005 [US1] Implement `get_query_embedding(query_text: str)` function using Cohere `embed-english-v3.0` model in `backend/retrieve.py`.
- [x] T006 [US1] Implement `perform_qdrant_search(query_embedding: list[float], top_k: int = 5)` function to perform vector similarity search in `rag_embedding` collection in `backend/retrieve.py`.
- [x] T007 [US1] Implement `display_results(search_results: list[dict])` function to print retrieved text and metadata (URL, module, chunk index) in a readable format in `backend/retrieve.py`.
- [x] T008 [US1] Implement `main()` function to accept user query, orchestrate embedding, search, and display in `backend/retrieve.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T009 Update `backend/README.md` to include instructions for running `retrieve.py`.
- [x] T010 Add robust error handling for API calls and Qdrant connection in `backend/retrieve.py`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately (reusing existing environment).
- **Foundational (Phase 2)**: No dependencies - can start immediately (reusing existing client setups).
- **User Story 1 (Phase 3)**: Depends on the existing `backend/` environment (Spec-1).
- **Polish (Final Phase)**: Depends on User Story 1 being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after the existing `backend/` environment is established (Spec-1).

### Within Each User Story

- Environment variable loading and client initialization before other functions.
- Query embedding before Qdrant search.
- Qdrant search before result display.
- Core functions before orchestration in `main()`.

### Parallel Opportunities

- The tasks for User Story 1 (T002-T007) are largely sequential due to their interdependencies within a single script. However, the initial setup (T001-T004) could be done quickly.
- The polish tasks (T009-T010) can be implemented after the core functionality of User Story 1 is complete, potentially in parallel if desired.

---

## Parallel Example: User Story 1 (Limited Parallelism)

```bash
# Initial setup of the script and its core components:
Task: "Create backend/retrieve.py script"
Task: "Load environment variables (COHERE_API_KEY, QDRANT_API_KEY, QDRANT_URL) from .env in backend/retrieve.py"
Task: "Initialize Cohere client in backend/retrieve.py"
Task: "Initialize Qdrant client, connecting to rag_embedding collection in backend/retrieve.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Ensure existing `backend/` environment is set up (from Spec-1).
2. Complete Phase 3: User Story 1.
3. **STOP and VALIDATE**: Test User Story 1 independently by running `retrieve.py` with various queries and inspecting results.
4. Deploy/demo if ready.

### Incremental Delivery

1. Ensure existing `backend/` environment is set up.
2. Complete User Story 1 → Test independently → Deploy/Demo (MVP!).
3. Add Polish tasks (e.g., improved error handling, documentation) → Test → Deploy/Demo.

### Parallel Team Strategy

With multiple developers:

1. One developer focuses on ensuring the existing `backend/` environment from Spec-1 is stable.
2. Another developer works on User Story 1.
3. Once User Story 1 is functional, polish tasks can be assigned.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
