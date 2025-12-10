---
id: 01
title: Update Project Constitution with Initial Scope
stage: constitution
date: 2025-12-10
surface: agent
model: gemini-1.5-pro
feature: none
branch: [BRANCH]
user: [USER]
command: /sp.constitution My goal is to act as the technical writer, architect, and code generator for a full university-level textbook and platform titled:

"Physical AI & Humanoid Robotics"

The output will be a Docusaurus textbook + RAG Chatbot + Personalization + Urdu Translation, built using Spec-Kit Plus and Claude Code workflows.

The audience is advanced CS/AI/Robotics students, so all writing must be highly technical, correct, and academically strong.

1. Scope of Work
I must create:

A. Full Docusaurus Textbook
Six modules:
1. ROS 2
2. Digital Twin (Gazebo & Unity)
3. NVIDIA Isaac
4. Vision-Language-Action (VLA)
5. Control Theory for Humanoids
6. Ethical & Legal Embodiment (ELSI)

Each chapter must include:
- Learning goals
- Deep theory
- Small Code examples (Python, ROS2, XML, YAML)
- Simulation steps
- Try-it-yourself activities
- Quiz
- Summary
- Glossary

All content must use perfect Docusaurus Markdown with:
- YAML front matter
- Syntax-highlighted code blocks
- Admonitions (::tip, ::note, ::warning)
- Clear heading hierarchy
- Mermaid diagrams

B. RAG Chatbot System
Using: FastAPI, Qdrant Cloud, Neon Postgres, OpenAI Agents/ChatKit.
Chatbot must answer only from book content and support selected-text answering. Chat history stored in Postgres.

C. Authentication (BetterAuth)
Signup must collect user hardware, experience level, and background.

D. Personalization
Each chapter includes a “Personalize for Me” button that adjusts content based on user profile.

E. Urdu Translation
Each chapter includes “Translate to Urdu.” Formatting must remain identical; code stays in English.

F. Reusable Subagents & Skills
Using Spec-Kit Plus workflow (sp.specify → sp.plan → sp.task → sp.implement).
Skills: ChapterWriter, ROS2Skill, GazeboSkill, IsaacSkill, VLASkill, QuizMaker, CodeGenerator, TranslationSkill, PersonalizationSkill, RAGSkill.

2. Writing & Coding Rules
- Be concise but deeply technical.
- Use accurate robotics terminology.
- Code must be runnable and correct.
- Always maintain Docusaurus formatting.

3. Safety Rules
- No unsafe robotics commands.
- Prefer simulation first.
- Provide warnings for real-world deployment.

4. Output Rules
- Markdown → Chapters
- JSON → Spec-Kit files
- Python → FastAPI, embeddings, ingestion
- TS/JS → Docusaurus + Chatbot UI

This constitution governs ALL behavior for writing, coding, planning, and generating the entire Physical AI & Humanoid Robotics textbook and platform.
labels: ["constitution", "initial-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:

---

## Prompt

/sp.constitution My goal is to act as the technical writer, architect, and code generator for a full university-level textbook and platform titled:

"Physical AI & Humanoid Robotics"

The output will be a Docusaurus textbook + RAG Chatbot + Personalization + Urdu Translation, built using Spec-Kit Plus and Claude Code workflows.

The audience is advanced CS/AI/Robotics students, so all writing must be highly technical, correct, and academically strong.

1. Scope of Work
I must create:

A. Full Docusaurus Textbook
Six modules:
1. ROS 2
2. Digital Twin (Gazebo & Unity)
3. NVIDIA Isaac
4. Vision-Language-Action (VLA)
5. Control Theory for Humanoids
6. Ethical & Legal Embodiment (ELSI)

Each chapter must include:
- Learning goals
- Deep theory
- Small Code examples (Python, ROS2, XML, YAML)
- Simulation steps
- Try-it-yourself activities
- Quiz
- Summary
- Glossary

All content must use perfect Docusaurus Markdown with:
- YAML front matter
- Syntax-highlighted code blocks
- Admonitions (::tip, ::note, ::warning)
- Clear heading hierarchy
- Mermaid diagrams

B. RAG Chatbot System
Using: FastAPI, Qdrant Cloud, Neon Postgres, OpenAI Agents/ChatKit.
Chatbot must answer only from book content and support selected-text answering. Chat history stored in Postgres.

C. Authentication (BetterAuth)
Signup must collect user hardware, experience level, and background.

D. Personalization
Each chapter includes a “Personalize for Me” button that adjusts content based on user profile.

E. Urdu Translation
Each chapter includes “Translate to Urdu.” Formatting must remain identical; code stays in English.

F. Reusable Subagents & Skills
Using Spec-Kit Plus workflow (sp.specify → sp.plan → sp.task → sp.implement).
Skills: ChapterWriter, ROS2Skill, GazeboSkill, IsaacSkill, VLASkill, QuizMaker, CodeGenerator, TranslationSkill, PersonalizationSkill, RAGSkill.

2. Writing & Coding Rules
- Be concise but deeply technical.
- Use accurate robotics terminology.
- Code must be runnable and correct.
- Always maintain Docusaurus formatting.

3. Safety Rules
- No unsafe robotics commands.
- Prefer simulation first.
- Provide warnings for real-world deployment.

4. Output Rules
- Markdown → Chapters
- JSON → Spec-Kit files
- Python → FastAPI, embeddings, ingestion
- TS/JS → Docusaurus + Chatbot UI

This constitution governs ALL behavior for writing, coding, planning, and generating the entire Physical AI & Humanoid Robotics textbook and platform.

## Response snapshot

The project constitution has been successfully updated to version 1.1.0 in `.specify/memory/constitution.md`. This update incorporates the detailed project vision, scope, core principles, and governance guidelines provided by the user. The version bump is minor, reflecting the addition of new content and expanded guidance.

## Outcome

- ✅ Impact: The project constitution is updated and aligned with the user's detailed requirements.
- 🧪 Tests: No tests were run as this was a documentation update.
- 📁 Files: One file was modified: `.specify/memory/constitution.md`.
- 🔁 Next prompts: Continue with project setup or specific feature development based on the updated constitution.
- 🧠 Reflection: The initial `constitution.md` template was more generic than expected, requiring adaptation to the structure implied by the user's detailed prompt. Using the user's prompt as the new template structure streamlined the process.

## Evaluation notes (flywheel)

- Failure modes observed: Attempted to use `create-phr.sh` which is a bash script, failing in a PowerShell environment. Remedied by using agent-native file operations.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
