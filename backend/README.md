# Embedding Pipeline Backend

This directory contains the Python backend for ingesting text from the physical-ai-humanoid-textbook Docusaurus site, generating Cohere embeddings, and storing them in a Qdrant vector database.

## Setup

1.  **Navigate to the `backend` directory**:
    ```bash
    cd backend
    ```

2.  **Create a Python virtual environment**:
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment**:
    *   **Windows (PowerShell)**:
        ```bash
        .\.venv\Scripts\Activate.ps1
        ```
    *   **Linux/macOS**:
        ```bash
        source ./.venv/bin/activate
        ```

4.  **Install dependencies**:
    ```bash
    uv pip install -r requirements.txt
    ```

5.  **Configure Environment Variables**:
    Create a `.env` file in the `backend` directory (same level as `main.py` and `requirements.txt`) based on the `.env.example` file.
    ```
    COHERE_API_KEY=your_cohere_api_key_here
    QDRANT_API_KEY=your_qdrant_api_key_here
    QDRANT_URL=your_qdrant_url_here
    ```

## Usage

### Run the Embedding Pipeline

The `main.py` script will crawl the configured Docusaurus site, extract text, chunk it, generate embeddings, and upsert them into your Qdrant collection.

Make sure your virtual environment is activated and `.env` is configured.
```bash
python main.py
```

### Verify Vector Search

The `verify_search.py` script allows you to test the semantic search functionality against the populated Qdrant collection.

Make sure your virtual environment is activated and `.env` is configured.
```bash
python verify_search.py
```
This script will prompt you to enter a query and display the top semantic search results.

### Run Retrieval and Validation Script

The `retrieve.py` script allows you to perform query embedding, Qdrant search, and display retrieved results for validation.

Make sure your virtual environment is activated and `.env` is configured.
```bash
python retrieve.py
```
This script will prompt you to enter a query and display relevant textbook chunks from Qdrant.

---

**Note**: This pipeline is designed to be re-run safely. The `create_collection()` function will recreate the collection, ensuring fresh data.
