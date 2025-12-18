---
id: 014
title: debug-cohere-api-key-loading
stage: misc
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 002-rag-agent-fastapi
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["debug", "backend", "api-key", "cohere", "huggingface"]
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

[User shared successful local curl but 403 on HF. Requested fix.]

## Response snapshot

Added a safe debug log to `backend/retrieval.py` that prints the length and first/last 2 characters of the `COHERE_API_KEY`. This allows the user to verify in Hugging Face Logs if the key is being read correctly and if there are any hidden spaces/newlines causing the 403 Forbidden error.

## Outcome

- ✅ Impact: Enables precise diagnosis of the 403 Forbidden error by verifying the loaded environment variable in the production environment.
- 🧪 Tests: N/A
- 📁 Files: `backend/retrieval.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: When local tests pass but cloud tests fail, verifying the environment state is the fastest path to resolution.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
