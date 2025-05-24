from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader

loader = TextLoader("docs_sample.txt")
documents = loader.load()

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)

def search_documents(query):
    docs = db.similarity_search(query)
    return [{"content": d.page_content} for d in docs]
