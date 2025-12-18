# Quickstart: RAG Agent Backend

## Prerequisites
- Python 3.10+
- Qdrant instance (running)
- Gemini API Key (Free tier)
- Cohere API Key

## Setup

1.  **Navigate to backend**:
    ```bash
    cd backend
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables**:
    Create `.env` in `backend/`:
    ```env
    GEMINI_API_KEY=your_gemini_key
    COHERE_API_KEY=your_cohere_key
    QDRANT_URL=http://localhost:6333
    QDRANT_API_KEY=your_qdrant_key # if applicable
    ```

4.  **Run Server**:
    ```bash
    uvicorn main:app --reload
    ```

## Usage

**Ask a question**:
```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"query": "What is ROS 2?"}'
```

