---
id: 003
title: Physical AI Humanoid Robotics Constitution
stage: constitution
date: 2025-12-16
surface: agent
model: gemini
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "update", "v2.0.0", "scope-expansion", "book", "chatbot"]
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
/sp.constitution /sp.constitution

Project: Physical AI & Humanoid Robotics — Book + RAG Chatbot

Principles:
- Technical accuracy (ROS 2, Gazebo, Unity, Isaac, VLA, RAG)
- Clear, step-by-step explanations for intermediate AI/robotics learners
- Reproducible code and tutorials
- Consistent terminology and engineering tone

Book Standards:
- Structure: 8 core chapters (ROS2, Gazebo/Unity, Isaac, Nav2/SLAM, URDF, Sensors, VLA, Capstone)
- Word count: 30k–50k words
- 20+ runnable code examples
- Use diagrams when needed
- Flesch-Kincaid grade 9–11

RAG Chatbot Standards:
- Answers strictly from book content
- “Selected-text only” mode required
- Stack: FastAPI + OpenAI Agents/ChatKit + Qdrant + Neon Postgres
- Clean chunking & deterministic retrieval

Citations:
- IEEE style
- Min 30 credible sources (ROS docs, NVIDIA docs, robotics papers)
- Zero plagiarism tolerance

Constraints:
- Built using Spec-Kit Plus + Claude Code
- Final deployment: Docusaurus on GitHub Pages
- Chatbot fully embedded and functional

Success Criteria:
- Book builds & deploys
- Chatbot answers accurately
- All content verifiable and runnable

## Response snapshot

Updated constitution to v2.0.0 (MAJOR) to reflect expanded scope covering both the Textbook content and the RAG Chatbot. Defined 4 new core principles: Technical Accuracy, Learner Clarity, Reproducible Code, and Consistent Tone. Integrated specific Book and Chatbot standards, including the previously defined tech stack.

## Outcome

- ✅ Impact: Constitution updated to v2.0.0
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Merged content and tech requirements into a single governance doc.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): None
