# Tasks: Vision-Language-Action (VLA) LLM Cognitive Planning

**Input**: Design documents from `/specs/002-vla-llm-cognitive-planning/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project directory structure for a backend service: `src/`, `src/api/`, `src/services/`, `config/`, `tests/`.
- [ ] T002 Initialize Python project with `poetry` or `pipenv` and add dependencies: `fastapi`, `uvicorn`, `requests`, `pyyaml`, `openai` (or equivalent LLM client), `pydantic`.
- [ ] T003 [P] Configure `pytest` for testing in `pyproject.toml` or `setup.cfg`.
- [ ] T004 [P] Setup environment variable management for API keys (e.g., `.env` file and `python-dotenv`).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Define supported ROS 2 action schemas (`nav2_action_server/NavigateToPose`, `grasp_action_server/GraspObject`) with their required parameters in `config/ros_actions.yaml`.
- [ ] T006 Implement a utility function in `src/utils/action_schema_loader.py` to load and validate ROS 2 action schemas from `config/ros_actions.yaml`.
- [ ] T007 Implement basic logging configuration in `src/utils/logger.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Translate Natural Language Command to Robot Actions (Priority: P1) 🎯 MVP

**Goal**: A robotics engineer can send a natural language command to an API, and receive a structured YAML sequence of low-level ROS 2 actions.

**Independent Test**: Send a natural language command (e.g., "Go to the kitchen") to the `/vla/plan` API and verify a syntactically correct YAML output containing Nav2 actions. Send an ambiguous command (e.g., "Do something") and verify an appropriate `400 Bad Request` error response.

### Implementation for User Story 1

- [ ] T008 [US1] Implement FastAPI application initialization in `src/main.py`.
- [ ] T009 [US1] Implement the `/vla/plan` POST endpoint in `src/api/vla_planner.py` as defined in `specs/002-vla-llm-cognitive-planning/contracts/vla_plan_api.yaml`.
- [ ] T010 [P] [US1] Define `NaturalLanguageCommand`, `ROS2PlanResponse`, and `ErrorResponse` Pydantic models in `src/models/api_models.py` based on `vla_plan_api.yaml`.
- [ ] T011 [US1] Develop `LLMCognitivePlanner` class in `src/services/llm_planner.py` to interact with the chosen LLM API (e.g., OpenAI).
- [ ] T012 [US1] Design the LLM prompt within `src/services/llm_planner.py` to interpret natural language commands and generate an intermediate "Cognitive Plan" (e.g., a structured JSON list of intended actions and parameters).
- [ ] T013 [US1] Implement error handling for LLM API calls within `src/services/llm_planner.py`.
- [ ] T014 [US1] Develop `ActionTranslator` class in `src/services/action_translator.py` to translate the LLM's "Cognitive Plan" (intermediate JSON) into the structured YAML `ROS 2 Action Sequence`.
- [ ] T015 [US1] Integrate action schema validation from `src/utils/action_schema_loader.py` into `src/services/action_translator.py` to ensure generated actions conform to `config/ros_actions.yaml`.
- [ ] T016 [US1] Implement logic within `src/api/vla_planner.py` to detect ambiguous or physically impossible commands based on the `LLMCognitivePlanner`'s output and return `400 Bad Request` with an `ErrorResponse` (FR-006, FR-007).
- [ ] T017 [US1] Integrate logging from `src/utils/logger.py` for LLM interactions and planning results within `src/services/llm_planner.py` and `src/api/vla_planner.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and documentation

- [ ] T018 Write the VLA overview section for `docs/04-vla/01_llm_cognitive_planning.md`, covering the Vision-Language-Action paradigm.
- [ ] T019 Write the Voice-to-Action (Whisper) component section for `docs/04-vla/01_llm_cognitive_planning.md`, describing how voice input could integrate with VLA.
- [x] T020 Write the detailed Cognitive Planning section for `docs/04-vla/01_llm_cognitive_planning.md`, including LLM planning theory and a code block for prompt-to-YAML conversion.
- [ ] T021 Code cleanup and refactoring across the codebase.
- [ ] T022 Performance optimization to meet the 5-second goal for plan generation.
- [ ] T023 Run quickstart validation, verifying the examples in `specs/002-vla-llm-cognitive-planning/quickstart.md` are accurate and runnable.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational phase completion
- **Polish (Phase 4)**: Depends on User Story 1 completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Pydantic models (T010) before API endpoint (T009) or services (T011, T014).
- LLM Planner (T011) and Action Translator (T014) can be developed in parallel, but their integration (T009, T015, T016, T017) depends on both.
- Actions schema loader (T006) and logger (T007) must be complete before their integration tasks in Phase 3.

### Parallel Opportunities

- Tasks T001-T004 (Setup) can run in parallel.
- Tasks T005-T007 (Foundational) can run in parallel.
- Within User Story 1: T010 can be done in parallel. T011 and T014 can also be done in parallel.
- Tasks T018-T020 (Documentation) can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add Polish & Cross-Cutting Concerns → Enhance and refine

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    *   Developer A: User Story 1 (T008-T017)
    *   Developer B: Polish & Cross-Cutting Concerns (T018-T023), focusing on documentation and general improvements.

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
