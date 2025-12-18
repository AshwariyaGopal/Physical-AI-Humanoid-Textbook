---
id: 021
title: expose-gemini-generation-errors
stage: misc
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 002-rag-agent-fastapi
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["debug", "gemini", "generation-error", "api-key"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/agent.py
tests:
 - null
---

## Prompt

[User reported "I encountered an error while processing your request" which corresponds to a Gemini generation failure]

## Response snapshot

Updated `backend/agent.py` to return the actual error string from the Gemini API instead of a generic message. This will reveal if the failure is due to an invalid `GEMINI_API_KEY`, safety blocks, or rate limits.

## Outcome

- ✅ Impact: Significantly improved debuggability of the LLM generation phase by surfacing specific API errors to the user.
- 🧪 Tests: N/A
- 📁 Files: `backend/agent.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: Generic error messages are good for production but hinder development. Surfacing the raw error temporarily is the fastest way to fix API issues.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
