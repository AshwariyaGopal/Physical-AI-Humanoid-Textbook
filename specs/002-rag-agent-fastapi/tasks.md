# Tasks: RAG Agent Backend

**Feature**: `002-rag-agent-fastapi`
**Status**: Pending

## Phase 1: Setup

- [x] T001 Rename existing ingestion script to avoid conflicts with FastAPI app `- [x] T001 Rename backend/main.py to backend/ingest_pipeline.py`
- [x] T002 Update dependencies with FastAPI and Gemini SDK `- [x] T002 Update backend/requirements.txt`
- [x] T003 Create environment variable template `- [x] T003 Create backend/.env.example`

## Phase 2: Foundational

- [x] T004 Create Pydantic models for QueryRequest and QueryResponse `- [x] T004 Create backend/models.py`
- [x] T005 Implement retrieval logic (Cohere embed + Qdrant search) `- [x] T005 Create backend/retrieval.py`
- [x] T006 Initialize Gemini client and basic generation function `- [x] T006 Create backend/agent.py`

## Phase 3: User Story 1 - Textbook Q&A (P1)

**Goal**: Verify the agent can retrieve and reason over textbook content.
**Test**: Manual verification via python script or unit test invoking `agent.py` directly.

- [x] T007 [US1] Implement context assembly from retrieved chunks `- [x] T007 Update backend/agent.py`
- [x] T008 [US1] Implement grounded generation prompt for Gemini `- [x] T008 Update backend/agent.py`
- [x] T009 [US1] Implement source citation formatting in response `- [x] T009 Update backend/agent.py`

## Phase 4: User Story 2 - API Endpoint Query (P2)

**Goal**: Expose the functionality via HTTP.
**Test**: `curl` request to `/ask` endpoint returns 200 and valid JSON.

- [x] T010 [US2] Initialize FastAPI application `- [x] T010 Create backend/main.py`
- [x] T011 [US2] Implement POST /ask endpoint `- [x] T011 Update backend/main.py`
- [x] T012 [US2] Connect endpoint to agent logic `- [x] T012 Update backend/main.py`
- [x] T013 [US2] Add CORS middleware for frontend integration `- [x] T013 Update backend/main.py`

## Phase 5: User Story 3 - Handling Unrelated Queries (P3)

**Goal**: Gracefully handle off-topic or empty-result queries.
**Test**: Ask "What is the capital of France?" and verify rejection.

- [x] T014 [US3] Add fallback logic for empty retrieval results `- [x] T014 Update backend/retrieval.py`
- [x] T015 [US3] Update system prompt to strictly enforce textbook context `- [x] T015 Update backend/agent.py`
- [x] T016 [US3] Implement rate limit handling (429 retries) `- [x] T016 Update backend/agent.py`

## Phase 6: Polish

- [x] T017 Add comprehensive logging `- [x] T017 Update backend/main.py`
- [x] T018 Verify deployment readiness (no hardcoded paths/keys) `- [x] T018 Review backend/.env`

## Dependencies

1.  **Setup** (T001-T003) -> **Foundational** (T004-T006)
2.  **Foundational** -> **US1** (Logic)
3.  **US1** -> **US2** (API)
4.  **US2** -> **US3** (Refinement)

## Parallel Execution Examples

- **T004 (Models)** can be done alongside **T005 (Retrieval)** or **T006 (Agent)**.
- **T014 (Fallback)** and **T015 (Prompt)** can be worked on by separate developers once US1 is stable.

## Implementation Strategy

1.  **MVP**: Tasks T001-T012. Result: Functional API that answers questions.
2.  **Robustness**: Tasks T013-T016. Result: Production-ready agent handling errors and edge cases.
