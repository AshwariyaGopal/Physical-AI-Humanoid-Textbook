---

description: "Task list for Embedding Pipeline Setup"
---

# Tasks: Embedding Pipeline Setup

**Input**: Design documents from `/specs/001-embedding-pipeline/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Note**: The `plan.md` for this feature was not fully completed, so some technical context (like specific language version and project type) has been inferred from the previous steps and the `spec.md`.

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

- [x] T001 Create `backend` directory
- [x] T002 Initialize Python virtual environment with `uv` in `backend/.venv`
- [x] T003 Create `backend/requirements.txt` with `cohere`, `qdrant-client`, `beautifulsoup4`, `requests`, `python-dotenv`
- [x] T004 Install dependencies from `backend/requirements.txt` into `backend/.venv`
- [x] T005 Create `backend/.env.example` file

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Setup environment variable loading using `python-dotenv` in `backend/main.py`
- [x] T007 Initialize Cohere client with API key from environment variables in `backend/main.py`
- [x] T008 Initialize Qdrant client with URL and API key from environment variables in `backend/main.py`
- [x] T009 Define `COLLECTION_NAME` and `WEBSITE_BASE_URL` constants in `backend/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - End-to-End Ingestion (Priority: P1) 🎯 MVP

**Goal**: Run a script that crawls the textbook URLs, processes the text, and stores embeddings in Qdrant so that the RAG system has an up-to-date knowledge base.

**Independent Test**: Can be fully tested by providing a small list of URLs and verifying they appear in the Qdrant collection with correct vectors.

### Implementation for User Story 1

- [x] T010 [US1] Implement `get_all_urls(base_url: str)` function to collect Docusaurus URLs in `backend/main.py`
- [x] T011 [US1] Implement `extract_text_from_url(url: str)` function to fetch and clean HTML content in `backend/main.py`
- [x] T012 [US1] Implement `chunk_text(text: str, max_tokens: int, overlap: int)` function to split text into overlapping chunks in `backend/main.py`
- [x] T013 [US1] Implement `embed(texts: list[str])` function to generate Cohere embeddings in `backend/main.py`
- [x] T014 [US1] Implement `create_collection()` function to create or reuse Qdrant collection `rag_embedding` in `backend/main.py`
- [x] T015 [US1] Implement `save_chunk_to_qdrant(embeddings: list[list[float]], texts: list[str], urls: list[str])` function to upsert vectors with metadata in `backend/main.py`
- [x] T016 [US1] Implement `main()` function to orchestrate the full pipeline execution in `backend/main.py`
- [x] T017 [US1] Add logging for successful embedding storage within `save_chunk_to_qdrant` and `main` functions in `backend/main.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Vector Verification (Priority: P2)

**Goal**: Verify that the stored embeddings are semantically searchable so that I can trust the retrieval quality.

**Independent Test**: Perform a nearest-neighbor search in Qdrant using a query string relevant to the textbook content.

### Implementation for User Story 2

- [x] T018 [US2] Create `backend/verify_search.py` script
- [x] T019 [US2] Implement a function in `backend/verify_search.py` to connect to Qdrant
- [x] T020 [US2] Implement a function in `backend/verify_search.py` to perform a semantic search query against the `rag_embedding` collection
- [x] T021 [US2] Implement a `main` function in `backend/verify_search.py` to demonstrate searching and printing relevant results

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T022 Code cleanup and refactoring in `backend/main.py`
- [ ] T023 Implement more robust error handling for network requests in `backend/main.py`
- [ ] T024 Add retry logic for Cohere API calls to handle rate limits in `backend/main.py`
- [ ] T025 Improve URL crawling logic in `backend/main.py` to discover all relevant pages (e.g., sitemap parsing)
- [x] T026 Update documentation in a `README.md` in the `backend` directory with instructions for setup and running

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on User Story 1 for data in Qdrant.

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks (T001-T005) can run in parallel by different individuals if the project structure is agreed upon.
- All Foundational tasks (T006-T009) can run in parallel.
- Once Foundational phase completes, User Story 1 (T010-T017) can start.
- User Story 2 (T018-T021) can start once User Story 1 has populated the Qdrant database.
- Within User Story 1, tasks T010-T015 can be considered for parallel implementation if they can be developed and tested somewhat independently before final integration into `main()`.

---

## Parallel Example: User Story 1 (Partial)

```bash
# Example of parallel work on functions within main.py:
# (Note: These tasks are highly interdependent within a single file,
# so true parallelism is limited without careful coordination or breaking into separate files)

Task: "Implement get_all_urls(base_url: str) function to collect Docusaurus URLs in backend/main.py"
Task: "Implement extract_text_from_url(url: str) function to fetch and clean HTML content in backend/main.py"
Task: "Implement chunk_text(text: str, max_tokens: int, overlap: int) function to split text into overlapping chunks in backend/main.py"
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
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
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
