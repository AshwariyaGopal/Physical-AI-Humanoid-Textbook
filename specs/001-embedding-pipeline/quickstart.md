# Quickstart: Embedding Pipeline

## Prerequisites

- Python 3.10+
- Cohere API Key
- Qdrant Cloud Cluster URL + API Key

## Setup

1. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn requests beautifulsoup4 cohere qdrant-client pydantic
   ```

2. **Environment Variables**:
   Create a `.env` file:
   ```env
   COHERE_API_KEY=your_cohere_key
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_key
   ```

## Running the Pipeline (Standalone)

*Note: For development/testing purposes, you can run the pipeline script directly.*

```bash
python -m api.pipeline.ingest --urls https://example.com/page1 https://example.com/page2
```

## Running via API

1. **Start the Server**:
   ```bash
   uvicorn api.main:app --reload
   ```

2. **Trigger Ingestion**:
   ```bash
   curl -X POST http://localhost:8000/ingest \
     -H "Content-Type: application/json" \
     -d '{"urls": ["https://my-docusaurus-site.com/docs/intro"]}'
   ```

