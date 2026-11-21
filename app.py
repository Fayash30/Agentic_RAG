from src.data_loader import load_all_documents
from src.vector_store import FaissVectorStore
from src.search import RAGSearch
import os

# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    if os.path.exists("faiss_store/index.faiss"):
        store.load()
    else:
        store.build_from_documents(docs)
        store.save()
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)