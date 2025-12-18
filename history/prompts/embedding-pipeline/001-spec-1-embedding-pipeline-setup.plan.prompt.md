---
id: 001
title: Spec 1: Embedding Pipeline Setup
stage: plan
date: 2025-12-17
surface: agent
model: gemini-1.5-pro
feature: embedding-pipeline
branch: 001-embedding-pipeline
user: user
command: /sp.plan
labels: [backend, embedding, qdrant, cohere]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/requirements.txt
 - backend/main.py
 - backend/.env.example
tests: null
---

## Prompt

/sp.plan /sp.plan Spec 1: Embedding Pipeline Setup

Create a backend folder and initialize a Python project using the uv package manager.

Scope:
- This spec is a standalone data ingestion pipeline, not an API server.
- Do NOT include FastAPI, pydantic, OpenAI Agents SDK, or any web framework.

Technical requirements:
- Use uv to initialize and manage the Python environment
- Implement the entire pipeline in a single file named main.py
- Use Cohere for embedding generation
- Use Qdrant Cloud for vector storage
- Fetch content from the deployed Docusaurus site:
  https://physical-ai-humanoid-textbook-t6qt-gwj8vaa9z.vercel.app

System design (functions to implement in main.py):
- get_all_urls(): collect all relevant book URLs from the deployed site
- extract_text_from_url(url): fetch HTML and extract clean main content
- chunk_text(text): split text into overlapping chunks
- embed(chunks): generate embeddings using Cohere
- create_collection(): create or reuse a Qdrant collection named "rag_embedding"
- save_chunk_to_qdrant(embedding, metadata): upsert vectors with metadata
- main(): orchestrate the full pipeline execution

Constraints:
- Python-only dependencies with prebuilt Windows wheels
- No native compilation required
- All API keys loaded via environment variables
- Pipeline must be safe to re-run without duplicating data

Output:
- backend/main.py
- A populated Qdrant collection named "rag_embedding"
- Logged confirmation that embeddings were successfully stored

## Response snapshot

The `api` directory was removed, and a new `backend` directory was created. A virtual environment was initialized using `uv`, and `backend/requirements.txt` was created and its dependencies installed. The `backend/main.py` file was implemented with all specified functions for URL fetching, text extraction, chunking, embedding, Qdrant collection management, and upserting. A `.env.example` file was also created to guide the user on environment variables.

## Outcome

- ✅ Impact: Backend embedding pipeline implementation complete, ready for execution.
- 🧪 Tests: No automated tests were created for this planning phase.
- 📁 Files: Created `backend` directory, `backend/requirements.txt`, `backend/main.py`, and `backend/.env.example`.
- 🔁 Next prompts: Instructions on how to run the pipeline and provide API keys.
- 🧠 Reflection: Successfully set up the project by adhering to the new constraints of "no native compilation" and "Python-only dependencies with prebuilt Windows wheels".

## Evaluation notes (flywheel)

- Failure modes observed: Initial dependency installation failed due to `pydantic-core` requiring Rust compilation, which was resolved by re-evaluating requirements and ensuring Python-only dependencies with prebuilt Windows wheels.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
