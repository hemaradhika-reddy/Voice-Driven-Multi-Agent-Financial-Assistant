
from langchain_community.vectorstores import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

from langchain.prompts import PromptTemplate
prompt = PromptTemplate(
    input_variables=["query", "context"],
    template="As a financial analyst, provide a concise market brief for the query: {query}. Use the following context: {context}"
)
class LanguageAgent:
    def __init__(self, retriever):
        self.llm = HuggingFacePipeline.from_model_id(
            model_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
            task="text-generation",
            pipeline_kwargs={"max_new_tokens": 200}
        )
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever
        )
    
    def generate_narrative(self, query, context):
        response = self.qa_chain.run(query=query, context=context)
        return response