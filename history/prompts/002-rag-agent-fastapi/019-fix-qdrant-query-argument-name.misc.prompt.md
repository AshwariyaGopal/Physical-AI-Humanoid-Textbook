---
id: 019
title: fix-qdrant-query-argument-name
stage: misc
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 002-rag-agent-fastapi
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["fix", "qdrant", "query-argument", "fastembed"]
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

I'm having trouble accessing my knowledge base. Error: Unknown arguments: ['query_vector']

## Response snapshot

Adjusted the Qdrant `.query()` fallback in `backend/retrieval.py` to use `query=query_vector` instead of `query_vector=query_vector`. This aligns with the parameter naming convention in the FastEmbed-enabled Qdrant client, which is often automatically activated in newer environments.

## Outcome

- ✅ Impact: Resolved the argument mismatch error, allowing the fallback search logic to function correctly across different library versions.
- 🧪 Tests: N/A
- 📁 Files: `backend/retrieval.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: Library parameter naming changes are a common source of friction; providing the argument under the name the library expects (which is `query` in this specific mixin) is the fix.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
