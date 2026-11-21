# Traditional RAG | Modular Implementation

A modular **Retrieval-Augmented Generation (RAG)** system built with Python, LangChain, FAISS, Sentence Transformers, and Google Gemini.

The project implements an end-to-end RAG pipeline, from document ingestion and embedding generation to semantic retrieval and context-aware response generation.

## Architecture

```text
Documents
    |
    v
Document Loading
    |
    v
Text Splitting
    |
    v
Embedding Generation
    |
    v
FAISS Vector Store
    |
    v
Similarity Search <---- User Query
    |
    v
Retrieved Context
    |
    v
Google Gemini
    |
    v
Generated Response
```

## Features

- **Multi-format Document Loading:** PDF, TXT, CSV, Excel, Word, and JSON.
- **Text Splitting:** RecursiveCharacterTextSplitter with configurable chunk size and overlap.
- **Local Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`).
- **Vector Database:** FAISS for vector indexing and similarity search.
- **Persistent Storage:** Save and load FAISS indexes.
- **Top-K Retrieval:** Retrieve relevant document chunks based on query similarity.
- **LLM Integration:** Google Gemini for context-aware response generation.
- **Modular Design:** Independent components for loading, embedding, storage, and retrieval.

## Tech Stack

| Technology | Usage |
|---|---|
| Python | Core development |
| LangChain | Document processing |
| Sentence Transformers | Embeddings |
| FAISS | Vector storage and retrieval |
| Google Gemini | Response generation |
| NumPy | Vector operations |
| UV | Dependency management |

## Project Structure

```text
Agentic_RAG/
│
├── data/                  # Input documents
├── faiss_store/           # Persistent vector index
├── notebook/              # Experiments
│
├── src/
│   ├── data_loader.py     # Document ingestion
│   ├── embedding.py       # Splitting and embeddings
│   ├── vector_store.py    # FAISS operations
│   └── search.py          # Retrieval and LLM integration
│
├── app.py                 # Application entry point
├── requirements.txt
├── pyproject.toml
└── uv.lock
```

## RAG Pipeline

| Stage | Implementation |
|---|---|
| Ingestion | Load documents from multiple formats |
| Chunking | Recursive character-based splitting |
| Embedding | `all-MiniLM-L6-v2` |
| Indexing | FAISS with `IndexFlatL2` |
| Retrieval | Similarity search with Top-K |
| Generation | Google Gemini with retrieved context |

## Configuration

Set your Google Gemini API key in a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

## Key Learnings

- Implementing an end-to-end traditional RAG pipeline.
- Working with document loaders and text splitters.
- Generating and managing vector embeddings.
- Building persistent FAISS indexes.
- Implementing similarity-based retrieval.
- Connecting retrieved context with an LLM.
- Organizing RAG applications using modular Python components.

---