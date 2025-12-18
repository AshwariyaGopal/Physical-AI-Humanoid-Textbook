---
id: 026
title: handle-social-greetings-naturally
stage: polish
date: 2025-12-18
surface: agent
model: gemini-2.0-flash-exp
feature: 005-docusaurus-backend-integration
branch: 005-docusaurus-backend-integration
user: user
command: /sp.phr
labels: ["persona", "social-greetings", "grounded-rag", "ux"]
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

hi [User feedback: chatbot should respond to simple questions like hi/hello/how are you with simple answers instead of textbook summaries]

## Response snapshot

Modified the system prompt in `backend/agent.py` to include a specific instruction for social greetings. The agent is now allowed to respond naturally and briefly to "hi", "hello", "how are you", etc., without being forced to reference the textbook context. For all other queries, the strict RAG grounding and inline citation requirements remain in place.

## Outcome

- ✅ Impact: Improved the natural flow of the conversation, making the chatbot feel more like a "normal" assistant for introductory interactions while maintaining academic rigor for content questions.
- 🧪 Tests: N/A
- 📁 Files: `backend/agent.py`.
- 🔁 Next prompts: None
- 🧠 Reflection: Balancing strict grounding with natural conversation requires clear, prioritized instructions in the system prompt.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
