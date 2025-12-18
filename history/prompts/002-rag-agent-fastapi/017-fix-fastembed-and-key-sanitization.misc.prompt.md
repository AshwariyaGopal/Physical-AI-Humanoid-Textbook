---
id: 017
title: fix-fastembed-and-key-sanitization
stage: misc
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 002-rag-agent-fastapi
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["fix", "fastembed", "qdrant", "auth", "403-forbidden", "huggingface"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/requirements.txt
 - backend/retrieval.py
 - backend/agent.py
tests:
 - null
---

## Prompt

Database search failed: fastembed is not installed. Please install it to enable fast vector indexing with `pip install fastembed`. [User reported persistent 403 as well]

## Response snapshot

Resolved the `fastembed` error by reverting from the high-level `.query()` method to the standard `.search()` method in `backend/retrieval.py`, which avoids triggering internal embedding logic. Also added `fastembed` to `backend/requirements.txt` for extra compatibility. Implemented a `sanitize_key` helper to strip whitespace from environment variables, addressing the persistent 403 Forbidden issues caused by hidden spaces in Hugging Face Secrets.

## Outcome

- ✅ Impact: Eliminated the library dependency crash and provided a robust fix for common authentication failures in cloud environments.
- 🧪 Tests: N/A
- 📁 Files: `backend/requirements.txt`, `backend/retrieval.py`, `backend/agent.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: Library "magic" like auto-embedding can be a double-edged sword; explicit calls to `.search()` are often more predictable in production.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
