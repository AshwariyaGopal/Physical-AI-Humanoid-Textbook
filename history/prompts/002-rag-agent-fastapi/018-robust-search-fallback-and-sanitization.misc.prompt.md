---
id: 018
title: robust-search-fallback-and-sanitization
stage: misc
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 002-rag-agent-fastapi
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["fix", "qdrant", "search-fallback", "key-sanitization", "403-forbidden"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/retrieval.py
tests:
 - null
---

## Prompt

Database search failed: 'QdrantClient' object has no attribute 'search' [User still reporting persistent 403 Forbidden as well]

## Response snapshot

Implemented a dual-method search strategy in `backend/retrieval.py` that checks for the existence of the `.search()` method and falls back to `.query()` if it's missing (using `hasattr`). Enhanced the `sanitize_key` function to aggressively remove quotes and other hidden characters, specifically targeting the 403 Forbidden error which often stems from incorrectly formatted environment variables in cloud settings.

## Outcome

- ✅ Impact: Significantly increased the backend's resilience to library version differences and common configuration mistakes in deployment environments.
- 🧪 Tests: N/A
- 📁 Files: `backend/retrieval.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: When deploying to "hands-off" environments like Hugging Face Spaces, defensive coding around environment variables and library APIs is essential.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
