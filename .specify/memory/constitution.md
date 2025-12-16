<!--
Sync Impact Report:
- Version Change: 1.0.0 -> 2.0.0 (MAJOR)
- Rationale: Expanded project scope to include the Textbook itself, not just the Chatbot. Redefined Core Principles to cover content quality and pedagogical goals.
- Modified Principles: Replaced previous Chatbot-specific principles with broader project principles (Technical Accuracy, Clear Explanations, Reproducible Code, Consistent Tone).
- Added Sections: Book Standards, Citations.
- Modified Sections: RAG Chatbot Standards (incorporated previous Tech Stack), Constraints (Added Spec-Kit/Gemini), Success Criteria.
- Templates Requiring Updates:
  - .specify/templates/plan-template.md: ✅ Compatible.
  - .specify/templates/spec-template.md: ✅ Compatible.
  - .specify/templates/tasks-template.md: ✅ Compatible.
- Follow-up TODOs: None.
-->

# Physical AI & Humanoid Robotics — Book + RAG Chatbot Constitution

## Core Principles

### I. Technical Accuracy (ROS 2, Gazebo, Unity, Isaac, VLA, RAG)
The content must be authoritative, verifiable, and technically sound across all covered domains.
**Rules:**
- All technical claims MUST be verified against official documentation (ROS 2, NVIDIA Isaac, etc.) or peer-reviewed literature.
- The RAG Chatbot MUST provide answers strictly derived from this verified book content.
- Code examples MUST be functional and consistent with the documented theory.

### II. Clear, Step-by-Step Explanations for Learners
The material is designed for intermediate AI and robotics learners and must remain accessible yet rigorous.
**Rules:**
- Explanations MUST follow a logical progression, breaking down complex concepts into digestible steps.
- The reading level SHOULD target Flesch-Kincaid Grade 9–11.
- Avoid unnecessary jargon; define terms when first introduced.

### III. Reproducible Code and Tutorials
Learners must be able to replicate every result presented in the text.
**Rules:**
- All code provided MUST be runnable.
- Tutorials MUST be end-to-end complete, including necessary setup and dependencies.
- "Works on my machine" is not acceptable; environments must be specified.

### IV. Consistent Terminology and Engineering Tone
Maintain a professional, cohesive voice throughout the textbook and chatbot interactions.
**Rules:**
- Terminology MUST be consistent across chapters (e.g., sticking to standard ROS 2 naming conventions).
- The tone MUST be professional, objective, and engineering-focused.

## Standards

### Book Standards
- **Structure**: 8 core chapters (ROS2, Gazebo/Unity, Isaac, Nav2/SLAM, URDF, Sensors, VLA, Capstone).
- **Volume**: Target 30k–50k words.
- **Content**: Include 20+ runnable code examples and diagrams where necessary for clarity.
- **Readability**: Flesch-Kincaid Grade 9–11.

### RAG Chatbot Standards
- **Source of Truth**: Answers MUST be generated strictly from the book content.
- **Modes**: Support a "Selected-text only" mode that answers questions based solely on user-highlighted text.
- **Tech Stack**:
  - **Backend**: FastAPI
  - **LLM Orchestration**: OpenAI Agents SDK
  - **Chat UI**: OpenAI ChatKit SDK
  - **Vector DB**: Qdrant Cloud (Free Tier)
  - **Relational DB**: Neon Serverless Postgres
- **Retrieval**: Clean chunking and deterministic retrieval mechanisms MUST be implemented.

### Citations
- **Style**: IEEE.
- **Quantity**: Minimum 30 credible sources (ROS docs, NVIDIA docs, robotics papers).
- **Integrity**: Zero tolerance for plagiarism.

## Constraints

### Development & Operational
- **Tooling**: Built using Spec-Kit Plus + Gemini.
- **Deployment**: Final output MUST be a Docusaurus site deployed on GitHub Pages.
- **Integration**: The chatbot MUST be fully embedded and functional within the Docusaurus site.
- **Constraints**: No internet access for RAG generation; No fine-tuning.

## Success Criteria

### Measurable Outcomes
- **Build**: The book site builds and deploys successfully to GitHub Pages.
- **Accuracy**: The chatbot provides accurate answers with 0% hallucination (traceable to text).
- **Verifiability**: All code examples and tutorials are runnable and produce the described results.

## Governance

### Amendments
- Amendments require a formal review process.
- Changes to Core Principles or Mandatory Tech Stack constitute a MAJOR version change.

### Versioning
- **MAJOR**: Backward incompatible governance/principle removals or redefinitions.
- **MINOR**: New principle/section added or materially expanded guidance.
- **PATCH**: Clarifications, wording, typo fixes, non-semantic refinements.

**Version**: 2.0.0 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16
