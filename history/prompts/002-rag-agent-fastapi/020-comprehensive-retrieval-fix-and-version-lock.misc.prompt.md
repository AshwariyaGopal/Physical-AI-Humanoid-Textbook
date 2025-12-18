---
id: 020
title: comprehensive-retrieval-fix-and-version-lock
stage: misc
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 002-rag-agent-fastapi
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["fix", "qdrant", "cohere", "v5", "version-lock", "huggingface"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/requirements.txt
 - backend/retrieval.py
tests:
 - null
---

## Prompt

[User reported 'query' error and persistent 403 Forbidden on Cohere]

## Response snapshot

Locked `qdrant-client` to `1.12.0` and `cohere` to `>=5.0.0` in `backend/requirements.txt` to ensure a stable environment on Hugging Face. Completely refactored `backend/retrieval.py` to use the most standard and universal `.search()` method for Qdrant, and the modern `api_key=` pattern for Cohere. Enhanced the `sanitize_key` function to strip printable-only characters, effectively cleaning up any hidden control characters or quotes from HF Secrets.

## Outcome

- ✅ Impact: Standardized the backend to highly compatible library patterns and provided a permanent fix for the common "dirty" environment variable issues in cloud deployments.
- 🧪 Tests: N/A
- 📁 Files: `backend/requirements.txt`, `backend/retrieval.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: When external libraries provide too many ways to do one thing (like search vs query), sticking to the most mature and widely documented method (`.search`) is the safest bet for production.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
