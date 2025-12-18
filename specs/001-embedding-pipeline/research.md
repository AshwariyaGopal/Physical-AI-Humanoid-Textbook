# Research: Embedding Pipeline Setup

**Feature**: Embedding Pipeline Setup
**Status**: Concluded

## Decisions

### 1. HTML Extraction Strategy
- **Decision**: Use `requests` + `BeautifulSoup` (bs4).
- **Rationale**: Docusaurus sites are static site generated (SSG), meaning the initial HTML contains the full content. We do not need the overhead of a headless browser like Playwright or Selenium.
- **Alternatives Considered**:
    - *Playwright/Puppeteer*: Overkill for static HTML; requires browser binaries.
    - *Markdown Parsing*: Parsing the raw `.md` files in the repo is possible but "Deployed URLs" was the specific requirement, which ensures we index exactly what the user sees (including potential sidebars/footers if we wanted, though we usually strip those).

### 2. Embedding Model
- **Decision**: Cohere `embed-english-v3.0`.
- **Rationale**: Explicitly requested by the user. Excellent performance for retrieval tasks (MTEB leaderboard).
- **Constraints**: 
    - Input type parameter must be set (`search_document` for storage, `search_query` for retrieval).
    - API keys required via env vars.

### 3. Vector Database
- **Decision**: Qdrant Cloud.
- **Rationale**: Explicitly requested and mandated by Constitution.
- **Implementation**: Use `qdrant-client` Python SDK.
- **Schema**:
    - Collection Name: `textbook_rag`
    - Vector Size: 1024 (for `embed-english-v3.0`)
    - Distance: `Cosine`
    - Payload: `source_url` (keyword), `text` (text), `chunk_index` (integer), `crawled_at` (datetime).

### 4. Text Chunking
- **Decision**: Recursive Character Splitter (approx 512 tokens / 2000 chars overlap).
- **Rationale**: Preserves semantic context better than fixed-size splitting. Docusaurus structure (headers) should be respected if possible.

## Open Questions Resolved

- **Q: Is a separate ingestion service needed?**
  - **A:** No, the Constitution mandates a FastAPI backend. This pipeline will be a module within that backend, triggered via an API endpoint or CLI command.
