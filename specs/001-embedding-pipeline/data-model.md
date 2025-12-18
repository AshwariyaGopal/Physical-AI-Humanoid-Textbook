# Data Model: Embedding Pipeline Setup

## Entities

### SourceDocument
Represents the raw content fetched from a URL.

| Field | Type | Description |
|-------|------|-------------|
| `url` | String | The normalized URL of the page. |
| `raw_html` | String | The full HTML content fetched. |
| `fetched_at` | DateTime | Timestamp of when the fetch occurred. |
| `status` | Enum | `SUCCESS`, `FAILED`. |

### TextChunk
A clean, discrete segment of text ready for embedding.

| Field | Type | Description |
|-------|------|-------------|
| `content` | String | The cleaned plain text. |
| `source_url` | String | Reference to the parent SourceDocument. |
| `chunk_index` | Integer | Order of the chunk in the original document. |
| `metadata` | Map | Additional context (e.g., page title). |

### VectorRecord
The payload structure stored in Qdrant.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Unique identifier for the point (deterministic UUIDv5 based on URL + chunk index). |
| `vector` | List[Float]| The embedding vector (1024 dims for Cohere v3). |
| `payload` | Map | Stored metadata for retrieval. |

## Payload Schema (Qdrant)

```json
{
  "source_url": "https://example.com/docs/intro",
  "text": "The text content of the chunk...",
  "chunk_index": 0,
  "title": "Introduction to ROS2"
}
```
