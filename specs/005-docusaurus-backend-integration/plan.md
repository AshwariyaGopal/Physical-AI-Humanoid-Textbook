# Implementation Plan: Docusaurus Backend Integration

**Branch**: `005-docusaurus-backend-integration` | **Date**: 2025-12-18 | **Spec**: [specs/005-docusaurus-backend-integration/spec.md](specs/005-docusaurus-backend-integration/spec.md)
**Input**: Feature specification from `/specs/005-docusaurus-backend-integration/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Integrate the RAG backend agent with the Docusaurus frontend by creating a floating chat widget. The widget will allow users to query the textbook content via the FastAPI backend and view grounded answers with source citations.

## Technical Context

**Language/Version**: TypeScript / React 18+ (Docusaurus default)
**Primary Dependencies**: React (built-in), Docusaurus core
**Storage**: Local Component State (React useState)
**Testing**: Manual verification, Browser DevTools
**Target Platform**: Web (Modern Browsers)
**Project Type**: web (frontend)
**Performance Goals**: Instant UI feedback, non-blocking network requests
**Constraints**: Minimal UI, use existing Docusaurus styles, connect to local/remote backend
**Scale/Scope**: Single component integration

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Tech Stack**: Compliant. Using Docusaurus/React (frontend) to connect to FastAPI (backend) as per Constitution.
- **RAG**: Compliant. Visualizing RAG outputs strictly.
- **Standards**: "Chat UI: OpenAI ChatKit SDK" in Constitution vs "Minimal UI" in Spec. **Decision**: Follow Spec (Minimal UI / Custom Component) as ChatKit might be overkill or mismatched for a simple "ask" widget in a textbook, and the spec explicitly requested "Minimal UI".

## Project Structure

### Documentation (this feature)

```text
specs/005-docusaurus-backend-integration/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── api.md
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── components/
│   └── ChatWidget/      # New component directory
│       ├── index.tsx    # Main Chat Widget logic
│       └── styles.module.css # Component styles
├── theme/               # Potential swizzling location (if needed)
docusaurus.config.ts     # Configuration updates (API URL)
```

**Structure Decision**: Create a dedicated `ChatWidget` component in `src/components` and integrate it into the layout (likely via `Layout` wrapper or `Root` swizzle if global, or just embedded in pages for MVP). Given the requirement for "without leaving the page", a global floating widget is best.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Custom UI vs ChatKit | Spec requested "Minimal UI", ChatKit adds dependency overhead | ChatKit might be too heavy/complex for simple Q&A |