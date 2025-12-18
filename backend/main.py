from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import QueryRequest, QueryResponse
from agent import generate_answer
import uvicorn
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="RAG Agent API", version="1.0.0")

# T013: CORS Middleware
origins = [
    "http://localhost:3000", # Default Docusaurus local port
    "https://physical-ai-humanoid-textbook-t6qt-gwj8vaa9z.vercel.app", # Production URL
    "*" # Allow all for now during dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    logger.info("Health check endpoint called")
    return {"message": "RAG Agent API is running"}

# T011, T012: /ask endpoint
@app.post("/ask", response_model=QueryResponse)
async def ask_agent(request: QueryRequest):
    logger.info(f"Received query: {request.query}")
    try:
        response = generate_answer(request.query)
        logger.info("Successfully generated response")
        return response
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
