import os
import google.generativeai as genai
from typing import List, Dict, Any
from dotenv import load_dotenv
from retrieval import retrieve_context
from models import QueryResponse, Source

# Load environment variables
load_dotenv()

import logging
logger = logging.getLogger(__name__)

# Sanitization function to remove hidden spaces/newlines from HF Secrets
def sanitize_key(key: str | None) -> str | None:
    return key.strip() if key else None

GEMINI_API_KEY = sanitize_key(os.getenv("GEMINI_API_KEY"))
if not GEMINI_API_KEY:
    logger.error("Environment variable GEMINI_API_KEY must be set.")
else:
    logger.info(f"Gemini API Key loaded: Length={len(GEMINI_API_KEY)}")

genai.configure(api_key=GEMINI_API_KEY)

# Use Gemini 1.5 Flash (Higher rate limits, stable)
MODEL_NAME = "gemini-1.5-flash" 

def generate_answer(query: str) -> QueryResponse:
    """
    Orchestrates the RAG process: Retrieve -> Reason -> Response.
    """
    # 1. Retrieve context
    try:
        retrieved_chunks = retrieve_context(query)
    except Exception as e:
        print(f"Retrieval error: {e}")
        return QueryResponse(
            answer=f"I'm having trouble accessing my knowledge base. Error: {str(e)}",
            sources=[]
        )
    
    if not retrieved_chunks:
        return QueryResponse(
            answer="I'm sorry, I couldn't find any relevant information in the textbook to answer your question.",
            sources=[]
        )

    # 2. Format prompt
    context_text = "\n\n".join([f"Source {i+1} ({chunk['url']}):\n{chunk['text']}" for i, chunk in enumerate(retrieved_chunks)])
    
    prompt = f"""You are a helpful and conversational AI assistant for a robotics textbook.
Your goal is to explain complex robotics concepts in a clear, professional, and friendly manner.

### Instructions:
1. **Social Greetings**: If the user says "hi", "hello", "how are you", or other social pleasantries, respond naturally and briefly as a friendly assistant. You do not need the textbook context for these.
2. **Factual Questions**: For all questions about robotics or textbook content, answer using ONLY the provided context below.
3. **Use inline citations** in the format [1], [2], etc., whenever you reference a specific piece of information from the context.
4. If a factual question is asked and the answer is not found in the context, politely state that you don't have that information in the textbook and suggest related topics they might find in the sources.
5. Keep your tone encouraging and educational.

Context:
{context_text}

Question: {query}

Helpful Answer:"""

    # 3. Generate response
    model = genai.GenerativeModel(MODEL_NAME)
    max_retries = 3
    base_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            answer_text = response.text
            break
        except Exception as e:
            if "429" in str(e) or "Resource exhausted" in str(e):
                import time
                if attempt < max_retries - 1:
                    time.sleep(base_delay * (2 ** attempt)) # Exponential backoff
                    continue
            
            # If not rate limit or out of retries
            print(f"Error generating content: {e}")
            return QueryResponse(answer=f"I encountered an error while generating the answer: {str(e)}", sources=[])
    else:
         return QueryResponse(answer="I am currently experiencing high traffic (Gemini rate limit). Please try again later.", sources=[])

    # 4. Format sources (Deduplicated by URL)
    sources = []
    seen_urls = set()
    for chunk in retrieved_chunks:
        url = chunk['url']
        if url not in seen_urls:
            sources.append(Source(
                url=url,
                title=chunk.get('title'),
                chunk_index=chunk['chunk_index']
            ))
            seen_urls.add(url)

    return QueryResponse(answer=answer_text, sources=sources)
