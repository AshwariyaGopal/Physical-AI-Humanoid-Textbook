# Data Model: Retrieval and validation of embedded textbook content for RAG readiness

**Date**: 2025-12-17
**Feature**: specs/001-rag-retrieval-validation/spec.md

## Entities

### UserQuery
Represents the natural language input provided by the user for retrieval.

**Attributes**:
- `text`: String - The raw natural language query.

### QueryEmbedding
The vector representation generated from the `UserQuery` using the Cohere embedding model.

**Attributes**:
- `vector`: List[float] - The numerical vector representation of the query.
- `model`: String - The name of the embedding model used (e.g., "embed-english-v3.0").

### RetrievedChunk
Represents a segment of textbook content returned from the Qdrant vector database as a result of a similarity search. This entity includes the original text, its embedding (if available), and associated metadata.

**Attributes**:
- `text`: String - The content of the textbook chunk.
- `url`: String - The URL of the source document from which the chunk was extracted.
- `module`: String - (Optional) The module or chapter name of the source document.
- `chunk_index`: Integer - (Optional) The sequential index of the chunk within its source document.
- `relevance_score`: Float - A score indicating the semantic similarity to the `UserQuery`.

## Relationships

- A `UserQuery` is transformed into a `QueryEmbedding`.
- A `QueryEmbedding` is used to search for `RetrievedChunk` entities in Qdrant.
- `RetrievedChunk` entities are stored in and retrieved from the `rag_embedding` Qdrant collection.
