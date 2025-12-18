# Feature Specification: Embedding Pipeline Setup

**Feature Branch**: `001-embedding-pipeline`
**Created**: 2025-12-17
**Status**: Draft
**Input**: User description: "Extract text from Deployed URLs, generate embeddings using cohere, and store them in a vector database for a unified AI textbook RAG system"

## User Scenarios & Testing

<!--
  Prioritized user journeys.
-->

### User Story 1 - End-to-End Ingestion (Priority: P1)

As a backend developer, I want to run a script that crawls the textbook URLs, processes the text, and stores embeddings in Qdrant so that the RAG system has an up-to-date knowledge base.

**Why this priority**: This is the core functionality required to populate the vector database. Without this, the RAG system has no data.

**Independent Test**: Can be fully tested by providing a small list of URLs and verifying they appear in the Qdrant collection with correct vectors.

**Acceptance Scenarios**:

1. **Given** a configuration file with a list of valid Docusaurus page URLs, **When** I execute the ingestion pipeline, **Then** the system should crawl each URL, extract text, and log successful insertion into Qdrant.
2. **Given** a URL that is 404 or unreachable, **When** I execute the pipeline, **Then** the system should log an error for that URL but continue processing the rest.
3. **Given** the pipeline has finished, **When** I query Qdrant collection info, **Then** the point count should match the number of processed text chunks.

---

### User Story 2 - Vector Verification (Priority: P2)

As a developer, I want to verify that the stored embeddings are semantically searchable so that I can trust the retrieval quality.

**Why this priority**: Ensures the quality of the data pipeline (cleaning + embedding) is sufficient for RAG.

**Independent Test**: Perform a nearest-neighbor search in Qdrant using a query string relevant to the textbook content.

**Acceptance Scenarios**:

1. **Given** the database is populated, **When** I perform a search query for a specific topic (e.g., "ROS2 nodes"), **Then** the returned results should contain text chunks relevant to that topic from the correct source URLs.

---

### Edge Cases

- **Empty Pages**: How does the system handle pages with no extractable text? (Should skip and log).
- **API Rate Limits**: How does the system handle Cohere API rate limits? (Should implement retry logic or fail gracefully with a message).
- **Large Content**: How does the system handle very long pages? (Must chunk text effectively before embedding).

## Requirements

### Functional Requirements

- **FR-001**: The system MUST accept a configuration source (e.g., file or sitemap URL) defining the target URLs to process.
- **FR-002**: The system MUST fetch HTML content from the specified URLs.
- **FR-003**: The system MUST clean the HTML content, removing tags, scripts, and styles to extract plain text.
- **FR-004**: The system MUST split the extracted text into chunks suitable for the embedding model context window.
- **FR-005**: The system MUST generate vector embeddings for each text chunk using the Cohere API (e.g., `embed-english-v3.0`).
- **FR-006**: The system MUST store the generated vectors, along with metadata (Source URL, Chunk Text, Chunk Index), in a Qdrant vector database.
- **FR-007**: The system MUST handle network errors (e.g., timeouts, 404s) during crawling without crashing the entire pipeline.
- **FR-008**: The system MUST allow configuration of API keys (Cohere) and Database connection details (Qdrant) via environment variables.

### Key Entities

- **SourceDocument**: Represents a single URL and its raw HTML content.
- **TextChunk**: A segment of cleaned text from a SourceDocument, ready for embedding.
- **VectorRecord**: The final data object stored in Qdrant, containing the embedding vector and payload (metadata).

## Success Criteria

### Measurable Outcomes

- **SC-001**: 100% of valid URLs provided in the input are processed (either successfully stored or explicitly logged as errors).
- **SC-002**: Text extraction removes 99% of HTML tags/boilerplate, leaving readable content.
- **SC-003**: Searching Qdrant for a specific phrase present in the source text returns the correct chunk as the top result (Top-1 Accuracy for exact matches).
- **SC-004**: The pipeline can process at least 1 page per second on average (excluding strict API rate limiting pauses).