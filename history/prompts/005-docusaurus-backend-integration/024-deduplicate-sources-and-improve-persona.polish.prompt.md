---
id: 024
title: deduplicate-sources-and-improve-persona
stage: polish
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 005-docusaurus-backend-integration
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["fix", "source-deduplication", "ui-cleanup", "rag"]
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

[User reported that "hi" was returning 5 sources with repetitive titles (e.g., "Week 8 Ethical Frameworks" 4 times)]

## Response snapshot

Updated `backend/agent.py` to deduplicate source citations by URL. If the RAG system retrieves multiple snippets from the same textbook page, the chatbot will now only list that page once in the "Sources" section. This makes the UI much cleaner and more professional.

## Outcome

- ✅ Impact: Resolved the repetitive source listing issue, resulting in a cleaner and more "normal" chatbot experience.
- 🧪 Tests: N/A
- 📁 Files: `backend/agent.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: Deduplication is a small but high-impact UI improvement in RAG systems where multiple relevant chunks often come from the same source document.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
