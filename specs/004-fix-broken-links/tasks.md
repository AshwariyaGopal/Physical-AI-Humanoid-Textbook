---
description: "Task list for fixing broken links in Docusaurus"
---

# Tasks: Fix Broken Links & Build Errors

**Input**: Design documents from `/specs/004-fix-broken-links/`
**Prerequisites**: plan.md (required), spec.md (required)

## Phase 1: Setup

**Purpose**: Verify the current state and reproduce the error

- [ ] T001 [Setup] Run `npm run build` to confirm the broken link errors match the report

---

## Phase 2: User Story 1 - Fix Critical Module Links (Priority: P1)

**Goal**: Fix the 6 specific broken links reported in the Vercel build log

**Independent Test**: `npm run build` should pass the link checking phase for these specific paths

### Implementation for User Story 1

- [ ] T002 [US1] Update `src/components/ModuleCards/index.tsx` to change mixed-case links (e.g. `.../Week-1...`) to lowercase ID-based links (e.g. `.../week-1...`) for all 6 modules

**Checkpoint**: The explicit errors reported should be resolved.

---

## Phase 3: User Story 2 - Site-Wide Link Integrity (Priority: P2)

**Goal**: Ensure no other links are broken or case-mismatched

**Independent Test**: Manual navigation of navbar/footer without 404s

### Implementation for User Story 2

- [ ] T003 [US2] Audit `docusaurus.config.ts` navbar and footer links for case sensitivity (ensure `to: ...` paths match lowercase routes where applicable)
- [ ] T004 [US2] Audit `src/pages/index.tsx` for any other hardcoded links

**Checkpoint**: Site navigation is robust.

---

## Phase 4: User Story 3 - Build Validation (Priority: P3)

**Goal**: Verify final build success

**Independent Test**: `npm run build` exits with code 0

### Implementation for User Story 3

- [ ] T005 [US3] Run `npm run build` locally and verify output
- [ ] T006 [US3] (Optional) Start `npm start` and manually verify links in browser

**Checkpoint**: Project is ready for deployment.
