# Research: FastAPI Agent Backend with Gemini & RAG

## Decisions

### 1. LLM Provider: Google Gemini
- **Decision**: Use Google Gemini API (via `google-generativeai` SDK).
- **Rationale**:
  - Explicit user requirement: "Gemini free API key".
  - Feature spec requirement: "Gemini (Claude) API" (interpreted as Gemini due to "free API key" context).
  - Cost: Free tier available.
  - **Deviation from Constitution**: Constitution mentions "OpenAI Agents SDK". This feature specifically targets Gemini as an alternative/evolution.

### 2. Embedding Provider: Cohere
- **Decision**: Use Cohere API (via `cohere` SDK).
- **Rationale**:
  - Explicit user step: "Generate query embedding using Cohere".
  - Consistent with retrieval pipeline (implied).

### 3. Vector Database: Qdrant
- **Decision**: Use Qdrant (via `qdrant-client`).
- **Rationale**:
  - Explicit user requirement: "Load Qdrant collection 'rag_embedding'".
  - Existing infrastructure compatibility.

### 4. Backend Framework: FastAPI
- **Decision**: Use FastAPI.
- **Rationale**:
  - Standard Python async web framework.
  - Explicit user requirement.
  - Performance (ASGI).

## Implementation Details

### Gemini Integration
- **Library**: `google-generativeai`
- **Model**: `gemini-pro` (or `gemini-1.5-flash` if available/preferred for speed).
- **Authentication**: `GEMINI_API_KEY` env var.
- **Rate Limits**: Handle 429 errors (Free tier: 60 RPM). Implement retry logic (e.g., `tenacity` library).

### Retrieval Pipeline
1.  **Embed Query**: Cohere `embed` endpoint.
2.  **Search**: Qdrant `search` method on `rag_embedding` collection.
3.  **Context**: Format retrieved chunks (text + metadata) into a prompt for Gemini.

### Response Structure
-   **Answer**: Generated text.
-   **Sources**: List of `{ url, module, chunk_index }`.

## Unknowns & Risks
-   **Rate Limits**: Free tier might be tight. Need robust error handling.
-   **Context Window**: Ensure chunks fit within Gemini's context window (usually large enough, 32k+).