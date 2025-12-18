from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str

class Source(BaseModel):
    url: str
    title: Optional[str] = None
    module: Optional[str] = None
    chunk_index: int

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
