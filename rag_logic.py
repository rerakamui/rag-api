import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader

# 絶対パスでファイル読み込み（docs_sample.txt）
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir, "docs_sample.txt")
loader = TextLoader(filepath)
documents = loader.load()

# HuggingFaceの軽量モデルを使用（日本語対応モデルにも差替可）
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(documents, embeddings)

def search_documents(query):
    docs = db.similarity_search(query)
    return [{"content": d.page_content} for d in docs]
