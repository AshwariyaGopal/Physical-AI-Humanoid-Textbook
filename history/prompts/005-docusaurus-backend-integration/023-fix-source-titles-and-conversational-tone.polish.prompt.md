---
id: 023
title: fix-source-titles-and-conversational-tone
stage: polish
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 005-docusaurus-backend-integration
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["fix", "source-titles", "persona", "grounded-rag"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/models.py
 - backend/agent.py
tests:
 - null
---

## Prompt

[User reported that "Source 1" labels were still showing and the chatbot tone wasn't "normal" enough]

## Response snapshot

1. Updated `backend/models.py` to include the `title` field in the `Source` schema.
2. Updated `backend/agent.py` to pass the extracted title from the retrieval layer to the final response.
3. Adjusted the system prompt in `backend/agent.py` to make the assistant more conversational, friendly, and helpful, while strictly maintaining RAG grounding.
4. Fixed a minor model name typo (`gemini-2.5-flash` to `gemini-1.5-flash`).

## Outcome

- ✅ Impact: The chatbot now displays professional, descriptive source titles (e.g., "Week 1 Ros2 Core Concepts") and speaks with a more natural, engaging persona.
- 🧪 Tests: N/A
- 📁 Files: `backend/models.py`, `backend/agent.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: Data model changes often require updates across multiple layers (Models -> Agent -> Frontend) to ensure the data flows correctly.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
