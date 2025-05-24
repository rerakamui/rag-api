from langchain.document_loaders import TextLoader
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir, "docs_sample.txt")  # 正しいファイル名に注意
loader = TextLoader(filepath)

from fastapi import FastAPI, Query
from rag_logic import search_documents

app = FastAPI()

@app.get("/search")
def search(q: str = Query(...)):
    return {"results": search_documents(q)}
"# redeploy fix" 
"# redeploy fix" 

