import os
import logging
from qdrant_client import QdrantClient
from cohere import Client
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)

def sanitize_key(key: str | None) -> str | None:
    if not key: return None
    # Remove whitespace, quotes, and hidden control characters
    return "".join(c for c in key.strip() if c.isprintable()).strip("'").strip('"')

COHERE_API_KEY = sanitize_key(os.getenv("COHERE_API_KEY"))
QDRANT_API_KEY = sanitize_key(os.getenv("QDRANT_API_KEY"))
QDRANT_URL = sanitize_key(os.getenv("QDRANT_URL"))

try:
    # Use the latest Cohere Client pattern
    co = Client(api_key=COHERE_API_KEY)
    # Most universal Qdrant initialization
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
except Exception as e:
    logger.error(f"Initialization error: {e}")
    co = None
    qdrant_client = None

COLLECTION_NAME = "rag_embedding"

def embed_query(query: str) -> List[float]:
    if not co: raise RuntimeError("Cohere client not initialized.")
    try:
        # Latest v5+ embedding call
        response = co.embed(
            texts=[query],
            model="embed-english-v3.0",
            input_type="search_query"
        )
        return response.embeddings[0]
    except Exception as e:
        logger.error(f"Cohere error: {e}")
        if "403" in str(e):
            raise RuntimeError("403 Forbidden: Your Cohere API Key is being rejected. Check HF Secrets.")
        raise RuntimeError(f"Embedding failed: {str(e)}")

def search_chunks(query_text: str, query_vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
    if not qdrant_client: raise RuntimeError("Database client not initialized.")
    
    try:
        # Standard .search is the most compatible across all 1.x versions
        hits = qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=limit,
            with_payload=True
        )
        
        return [{
            "text": hit.payload.get("text", "No content"),
            "url": hit.payload.get("url", "#"),
            "title": hit.payload.get("url", "").split('/')[-1].replace('-', ' ').title(),
            "score": hit.score,
            "chunk_index": hit.id if isinstance(hit.id, (int, str)) else 0 
        } for hit in hits]
    except Exception as e:
        logger.error(f"Search error: {e}")
        raise RuntimeError(f"Database search failed: {str(e)}")

def retrieve_context(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    return search_chunks(query, embed_query(query), limit=top_k)
