# Implementation Plan: RAG Agent Backend

**Branch**: `002-rag-agent-fastapi` | **Date**: 2025-12-18 | **Spec**: [specs/002-rag-agent-fastapi/spec.md](specs/002-rag-agent-fastapi/spec.md)
**Input**: Feature specification from `/specs/002-rag-agent-fastapi/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement the backend RAG agent logic using FastAPI, Qdrant, and Google Gemini. The agent will expose a `/ask` endpoint that takes a user query, retrieves relevant chunks from Qdrant (using Cohere embeddings), and uses Gemini to generate a grounded answer citing the sources.

## Technical Context

**Language/Version**: Python 3.10+
**Primary Dependencies**: FastAPI, uvicorn, google-generativeai, cohere, qdrant-client, python-dotenv
**Storage**: Qdrant (Vector DB), In-memory (Config)
**Testing**: pytest, httpx
**Target Platform**: Local/Server (Python)
**Project Type**: web (backend)
**Performance Goals**: <5s latency (dominated by LLM), handle rate limits
**Constraints**: Free Gemini API key (60 RPM), Qdrant Cloud (Free Tier)
**Scale/Scope**: Single endpoint, stateless

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Tech Stack**: Deviation. Constitution asks for OpenAI Agents SDK. Feature Spec/Prompt asks for Gemini. **Decision**: Follow Feature Spec (Gemini).
- **RAG**: Deviation. Constitution says "No internet access for RAG". **Decision**: Compliant (using local/Qdrant data, not web search).
- **Tooling**: Compliant (Spec-Kit + Gemini).

## Project Structure

### Documentation (this feature)

```text
specs/002-rag-agent-fastapi/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── openapi.yaml
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── main.py              # FastAPI app and endpoint
├── agent.py             # Gemini integration logic
├── retrieval.py         # Qdrant/Cohere integration logic
├── models.py            # Pydantic data models
├── requirements.txt     # Dependencies
└── .env                 # Environment variables
```

**Structure Decision**: Use `backend/` directory for the Python service.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Using Gemini instead of OpenAI | Requirement | OpenAI is paid/not requested |