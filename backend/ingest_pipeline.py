import os
import requests
from bs4 import BeautifulSoup
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
WEBSITE_BASE_URL = "https://physical-ai-humanoid-textbook-t6qt-gwj8vaa9z.vercel.app"

def get_all_urls(base_url: str) -> list[str]:
    """
    Collects all relevant book URLs from the deployed Docusaurus site.
    This is a simplified version; a more robust solution would crawl the site.
    """
    print(f"Fetching URLs from {base_url}...")
    response = requests.get(base_url)
    response.raise_for_status() # Raise an exception for HTTP errors
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    urls = []
    # Find links related to documentation or modules
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/docs/Module-') and not href.endswith('/'):
            full_url = base_url.rstrip('/') + href
            urls.append(full_url)
    return list(set(urls)) # Remove duplicates

def extract_text_from_url(url: str) -> str:
    """
    Fetches HTML content from a URL and extracts clean main content.
    """
    print(f"Extracting text from {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Remove script, style, and other non-content elements
    for script in soup(["script", "style", "header", "footer", "nav", "aside"]):
        script.extract()
    
    # Get text
    text = soup.get_text()
    
    # Break into lines and remove leading/trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def chunk_text(text: str, max_tokens: int = 250, overlap: int = 50) -> list[str]:
    """
    Splits text into overlapping chunks.
    This is a token-based chunking, assuming 1 token is roughly 4 characters.
    A more precise solution would use a tokenizer.
    """
    print("Chunking text...")
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        word_length = len(word)
        # Rough token estimation: 1 token is approx 4 characters
        # Add 1 for space between words
        if current_length + word_length + 1 <= max_tokens * 4:
            current_chunk.append(word)
            current_length += word_length + 1
        else:
            chunks.append(" ".join(current_chunk))
            # Create overlap: approximately 'overlap' tokens
            # If overlap is 50 tokens, it's roughly 200 characters or 50 words
            overlap_count = int(overlap * 0.5) # Roughly half a word per token
            overlap_words = current_chunk[-overlap_count:] if len(current_chunk) > overlap_count else []
            current_chunk = overlap_words + [word]
            current_length = sum(len(w) for w in current_chunk) + len(current_chunk) - 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def embed(texts: list[str]) -> list[list[float]]:
    """
    Generates embeddings using Cohere.
    """
    print(f"Generating embeddings for {len(texts)} chunks using Cohere...")
    response = co.embed(
        texts=texts,
        model="embed-english-v3.0", # Using a common embedding model
        input_type="search_document"
    )
    return response.embeddings

def create_collection():
    """
    Creates or reuses a Qdrant collection named "rag_embedding".
    """
    print(f"Ensuring Qdrant collection '{COLLECTION_NAME}' exists...")
    try:
        qdrant_client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE), # Cohere embed-english-v3.0 has 1024 dimensions
        )
        print(f"Collection '{COLLECTION_NAME}' recreated.")
    except Exception as e:
        print(f"Could not recreate collection (it might already exist or there's another issue): {e}")
        if not qdrant_client.collection_exists(collection_name=COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' does not exist, attempting to create it.")
            qdrant_client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE),
            )
            print(f"Collection '{COLLECTION_NAME}' created.")
        else:
            print(f"Collection '{COLLECTION_NAME}' already exists, reusing it.")

def save_chunk_to_qdrant(embeddings: list[list[float]], texts: list[str], urls: list[str]):
    """
    Upserts vectors with metadata to Qdrant.
    """
    print(f"Upserting {len(embeddings)} vectors to Qdrant...")
    
    # Qdrant upsert expects points as (id, vector, payload)
    # Generate unique IDs for each point. For simplicity, we use an incrementing integer.
    # In a production system, you might use a UUID or a hash of the content.
    points = []
    for i, (embedding, text, url) in enumerate(zip(embeddings, texts, urls)):
        points.append(models.PointStruct(
            id=i, # Simple ID, can be made more robust
            vector=embedding,
            payload={"text": text, "url": url}
        ))
    
    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=points
    )
    print(f"Successfully upserted {len(embeddings)} embeddings to Qdrant.")

def main():
    print("Starting embedding pipeline...")
    create_collection()
    
    all_site_urls = get_all_urls(WEBSITE_BASE_URL)
    if not all_site_urls:
        print("No URLs found to process.")
        return

    all_chunks = []
    all_chunk_urls = []

    for url in all_site_urls:
        text = extract_text_from_url(url)
        if text:
            chunks = chunk_text(text)
            all_chunks.extend(chunks)
            all_chunk_urls.extend([url] * len(chunks)) # Store the URL for each chunk
        else:
            print(f"Warning: No text extracted from {url}")

    if not all_chunks:
        print("No chunks generated from extracted text.")
        return
        
    embeddings = embed(all_chunks)
    
    save_chunk_to_qdrant(embeddings, all_chunks, all_chunk_urls)
    print("Embedding pipeline finished successfully!")

if __name__ == "__main__":
    main()
