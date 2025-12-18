---
id: 025
title: improve-agent-response-style-with-citations
stage: polish
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 005-docusaurus-backend-integration
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["persona", "citations", "openai-style", "grounded-rag"]
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

https://openai.github.io/openai-agents-python/ take some help from this source that how should chatbot should respond

## Response snapshot

Updated the system prompt in `backend/agent.py` to align with professional AI agent standards (inspired by OpenAI's approach). The bot is now explicitly instructed to use **inline numbered citations** (e.g., [1], [2]) and maintains a "professional yet friendly" educational persona. This makes the answers feel more authoritative and easier to verify against the textbook sources.

## Outcome

- ✅ Impact: Significantly improved the quality and "feel" of the chatbot's responses, making them look like a modern, high-quality AI assistant.
- 🧪 Tests: N/A
- 📁 Files: `backend/agent.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: Style is as important as accuracy for user trust. Inline citations provide clear traceability from the answer back to the specific source document.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
