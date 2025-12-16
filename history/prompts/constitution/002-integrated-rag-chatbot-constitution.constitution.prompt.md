---
id: 002
title: Integrated RAG Chatbot Constitution
stage: constitution
date: 2025-12-16
surface: agent
model: gemini
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "setup", "rag", "chatbot"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  null
---

## Prompt

$ARGUMENTS
/sp.constitution

Project: Integrated RAG Chatbot for AI-Native Textbook

Core principles:
- Zero hallucination (context-only answers)
- Deterministic and reproducible behavior
- AI-native, agent-based design
- Seamless embedding inside Docusaurus

Key standards:
- All answers must be traceable to textbook content or user-selected text
- Vector retrieval must precede generation
- Selected-text questions must bypass retrieval and use only the provided text
- Fixed refusal for out-of-scope queries:
  “This topic is not covered in the textbook.”

Required technologies:
- Backend: FastAPI
- LLM orchestration: OpenAI Agents SDK
- Chat UI: OpenAI ChatKit SDK
- Vector DB: Qdrant Cloud (Free Tier)
- Relational DB: Neon Serverless Postgres

Constraints:
- No internet or external knowledge access
- No fine-tuning
- No embeddings in relational DB
- Implementation must strictly follow specs

Functional requirements:
- Answer textbook-based questions
- Answer questions from user-selected text only
- Enforce context-only reasoning
- Return concise, educational responses

Data requirements:
- Deterministic chunking of textbook content
- Metadata per chunk: module, chapter, language
- User data stored only in Neon Postgres

Success criteria:
- 0% hallucination
- Deterministic refusals
- Spec-driven implementation matches behavior exactly

## Response snapshot

Updated constitution to v1.0.0 with 4 core principles: Zero Hallucination, Deterministic Behavior, AI-Native Design, Seamless Docusaurus Embedding. Established strict technology stack (FastAPI, OpenAI Agents/ChatKit, Qdrant, Neon) and constraints.

## Outcome

- ✅ Impact: Constitution established v1.0.0
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Defined strict tech stack constraints.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): None
