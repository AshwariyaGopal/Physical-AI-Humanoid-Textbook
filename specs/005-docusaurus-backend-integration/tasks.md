# Tasks: Docusaurus Backend Integration

**Input**: Design documents from `/specs/005-docusaurus-backend-integration/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `src/components/ChatWidget` directory structure
- [X] T002 Initialize `src/components/ChatWidget/styles.module.css` with base layout styles
- [X] T003 Configure `docusaurus.config.ts` to include `BACKEND_URL` in custom fields

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [X] T004 Define `ChatMessage`, `Source`, and `AppState` types in `src/components/ChatWidget/index.tsx`
- [X] T005 Create base `ChatWidget` component shell in `src/components/ChatWidget/index.tsx`
- [X] T006 Implement `useCustomFields` hook usage in `ChatWidget` to retrieve `BACKEND_URL`

**Checkpoint**: Foundation ready - UI components and configuration are accessible.

---

## Phase 3: User Story 1 - Ask Question via UI (Priority: P1) 🎯 MVP

**Goal**: Implement the chat interface and local message management.

**Independent Test**: User can type a question, hit enter, and see their question appear in the chat history.

### Implementation for User Story 1

- [X] T007 [US1] Create input field and submit button in `src/components/ChatWidget/index.tsx`
- [X] T008 [US1] Implement message history state using `useState` in `src/components/ChatWidget/index.tsx`
- [X] T009 [US1] Implement message list renderer in `src/components/ChatWidget/index.tsx`
- [X] T010 [US1] Add `handleSend` function to update state with user message and clear input

**Checkpoint**: User Story 1 functional - basic UI interaction works locally.

---

## Phase 4: User Story 2 - Backend Connection (Priority: P2)

**Goal**: Connect the UI to the FastAPI `/ask` endpoint.

**Independent Test**: User submits a question and receives a real answer from the backend visible in the UI.

### Implementation for User Story 2

- [X] T011 [US2] Implement `fetch()` POST request to `/ask` endpoint in `src/components/ChatWidget/index.tsx`
- [X] T012 [US2] Parse JSON response (answer and sources) and update assistant message in state
- [X] T013 [US2] Implement source citation renderer for assistant messages in `src/components/ChatWidget/index.tsx`
- [X] T014 [US2] Verify integration by testing with multiple textbook queries (e.g., "What is ROS 2?")

**Checkpoint**: User Story 2 functional - frontend successfully communicates with RAG backend.

---

## Phase 5: User Story 3 - Error Handling (Priority: P3)

**Goal**: Handle loading states and network/backend errors.

**Independent Test**: Spinner shows during request; error message shows if backend is down.

### Implementation for User Story 3

- [X] T015 [US3] Add `isLoading` state and render loading spinner in `src/components/ChatWidget/index.tsx`
- [X] T016 [US3] Add `error` state and render error alerts in `src/components/ChatWidget/index.tsx`
- [X] T017 [US3] Implement validation to prevent empty question submissions
- [X] T018 [US3] Test error handling by simulating backend failure (e.g., stopping the service)

**Checkpoint**: All user stories functional and robust.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T019 [P] Refine styles in `src/components/ChatWidget/styles.module.css` for "floating widget" look
- [X] T020 Integrate `ChatWidget` into global layout via `src/theme/Root.tsx` (or similar global wrapper)
- [X] T021 [P] Update `README.md` or `quickstart.md` with integration instructions
- [X] T022 Final verification: Confirm answers are grounded in book content via UI tests

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Phase 1.
- **User Story 1 (Phase 3)**: Depends on Phase 2.
- **User Story 2 (Phase 4)**: Depends on Phase 3.
- **User Story 3 (Phase 5)**: Depends on Phase 4 (can be done in parallel with US2 if separate files, but here in same file).
- **Polish (Phase 6)**: Depends on all user stories.

### Parallel Opportunities

- T019 (Styles) and T021 (Docs) can run in parallel.
- Most tasks are sequential as they modify `src/components/ChatWidget/index.tsx`.

---

## Implementation Strategy

### MVP First (User Story 1 & 2)

1. Complete Setup and Foundation.
2. Complete US1 (Basic UI).
3. Complete US2 (API ready).
4. **VALIDATE**: Real backend responses appearing in UI.

### Incremental Delivery

1. Foundation (Structure ready).
2. US1 (Input/List ready).
3. US2 (API ready).
4. US3 (Robustness ready).
5. Polish (UI/UX ready).
