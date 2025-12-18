# Data Model: RAG Agent

## Entities

### QueryRequest
Represents the user's question.

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| `query` | `string` | The natural language question. | Min length 1. |

### Source
Represents a reference to the source material used for the answer.

| Field | Type | Description |
|-------|------|-------------|
| `url` | `string` | URL of the source page. |
| `module` | `string` | Module name/ID. |
| `chunk_index` | `integer` | Index of the chunk in the source page. |

### QueryResponse
Represents the agent's answer and sources.

| Field | Type | Description |
|-------|------|-------------|
| `answer` | `string` | The generated answer from the agent. |
| `sources` | `Source[]` | List of sources used. |
