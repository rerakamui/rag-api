from fastapi import FastAPI, Query
from rag_logic import search_documents

app = FastAPI()

@app.get("/search")
def search(q: str = Query(...)):
    return {"results": search_documents(q)}
