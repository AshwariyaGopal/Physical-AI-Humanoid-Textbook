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
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

COLLECTION_NAME = "rag_embedding"

def semantic_search(query_text: str, top_k: int = 5) -> list[dict]:
    """
    Performs a semantic search in the Qdrant collection.
    """
    print(f"Searching for: '{query_text}'")
    
    # Generate embedding for the query
    query_embedding = co.embed(
        texts=[query_text],
        model="embed-english-v3.0",
        input_type="search_query"
    ).embeddings[0]

    # Perform search in Qdrant
    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=top_k,
        append_payload=True
    )

    results = []
    for hit in search_result:
        results.append({
            "score": hit.score,
            "text": hit.payload.get("text"),
            "url": hit.payload.get("url")
        })
    return results

def main():
    print("Starting vector verification script...")
    
    # Example query
    example_query = input("Enter a query to search in the textbook (e.g., 'ROS2 nodes'): ")
    if not example_query:
        example_query = "ROS2 nodes" # Default query if user enters nothing

    search_results = semantic_search(example_query)

    if search_results:
        print("\nSearch Results:")
        for i, result in enumerate(search_results):
            print(f"--- Result {i+1} (Score: {result['score']:.4f}) ---")
            print(f"URL: {result['url']}")
            print(f"Text: {result['text'][:200]}...") # Print first 200 chars of text
            print("-" * 20)
    else:
        print("No results found for your query.")
    
    print("Vector verification script finished!")

if __name__ == "__main__":
    main()
