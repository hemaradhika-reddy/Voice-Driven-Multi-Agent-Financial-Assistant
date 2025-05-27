# data_ingestion/doc_loader.py
from langchain.document_loaders import PyPDFLoader

class DocLoader:
    def load_pdf(self, file_path):
        try:
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            return documents
        except Exception as e:
            return f"Error loading PDF: {str(e)}"