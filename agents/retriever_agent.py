# agents/retriever_agent.py
from langchain.vectorstores import FAISS
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import pinecone

class RetrieverAgent:
    def __init__(self, pinecone_api_key=None, pinecone_index_name=None):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.faiss_store = None
        self.pinecone_store = None
        if pinecone_api_key and pinecone_index_name:
            pinecone.init(api_key=pinecone_api_key, environment="us-west1-gcp")
            self.pinecone_store = Pinecone(index_name=pinecone_index_name, embedding_function=self.embeddings)
    
    def index_documents(self, documents, use_pinecone=False):
        if use_pinecone and self.pinecone_store:
            self.pinecone_store.add_documents(documents)
        else:
            self.faiss_store = FAISS.from_documents(documents, self.embeddings)
    
    def retrieve(self, query, k=5, use_pinecone=False):
        if use_pinecone and self.pinecone_store:
            return self.pinecone_store.similarity_search(query, k=k)
        elif self.faiss_store:
            return self.faiss_store.similarity_search(query, k=k)
        return []