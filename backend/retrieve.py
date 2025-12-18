import os
from qdrant_client import QdrantClient, models
from cohere import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")

if not all([COHERE_API_KEY, QDRANT_API_KEY, QDRANT_URL]):
    raise ValueError("Environment variables COHERE_API_KEY, QDRANT_API_KEY, QDRANT_URL must be set.")

co = Client(COHERE_API_KEY)
# Use 'url' parameter as per previous fix
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

COLLECTION_NAME = "rag_embedding"

def get_query_embedding(query_text: str) -> list[float]:
    """
    Generates an embedding for a given query text using Cohere.
    """
    print(f"Generating embedding for query: '{query_text}'")
    try:
        response = co.embed(
            texts=[query_text],
            model="embed-english-v3.0",
            input_type="search_query"
        )
        return response.embeddings[0]
    except Exception as e:
        print(f"Error generating embedding with Cohere: {e}")
        return [] # Return empty list on error

def perform_qdrant_search(query_embedding: list[float], query_text: str, top_k: int = 5) -> list[dict]:
    """
    Performs a vector similarity search in the Qdrant collection.
    """
    if not query_embedding: # Handle empty embedding if generation failed
        return []
    
    print(f"Performing Qdrant search for top {top_k} results...")
    try:
        search_result = qdrant_client.query(
            collection_name=COLLECTION_NAME,
            query_embeddings=[query_embedding], # query expects a list of embeddings
            query_text=query_text, # Pass query_text
            n_results=top_k, # n_results instead of limit
            append_payload=True
        )
        results = []
        for hit in search_result:
            results.append({
                "score": hit.score,
                "text": hit.payload.get("text"),
                "url": hit.payload.get("url"),
                # Assuming 'module' and 'chunk_index' are available in metadata
                "module": hit.payload.get("module"), 
                "chunk_index": hit.payload.get("chunk_index")
            })
        return results
    except Exception as e:
        print(f"Error performing Qdrant search: {e}")
        return [] # Return empty list on error

def main():
    print("Starting RAG Retrieval Validation script...")
    
    query_text = input("Enter your query: ")
    if not query_text:
        print("Query cannot be empty. Exiting.")
        return

    query_embedding = get_query_embedding(query_text)
    if not query_embedding: # Exit if embedding generation failed
        print("Failed to generate query embedding. Exiting.")
        return

    search_results = perform_qdrant_search(query_embedding, query_text)
    display_results(search_results)
    
    print("RAG Retrieval Validation script finished!")

if __name__ == "__main__":
    main()
