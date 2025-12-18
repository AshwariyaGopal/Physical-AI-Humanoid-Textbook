# API Contract: Frontend Expectations

The frontend expects the backend to adhere to the following contract.

## Endpoints

### POST /ask

**Request**:
```json
{
  "query": "string"
}
```

**Response (Success)**:
```json
{
  "answer": "string",
  "sources": [
    {
      "url": "string",
      "chunk_index": 0
    }
  ]
}
```

**Response (Error)**:
Standard HTTP error codes (4xx, 5xx). The frontend should handle connection refused (network error) gracefully.
