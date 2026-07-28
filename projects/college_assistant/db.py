from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from pathlib import Path

load_dotenv()

embedding_model= MistralAIEmbeddings(model="mistral-embed")

def build_retriever(pdf_path: str):
    loader= PyPDFLoader(pdf_path)
    document= loader.load()
    
    splitter= RecursiveCharacterTextSplitter(
        chunk_size= 800,
        chunk_overlap= 100
    )
    
    chunks= splitter.split_documents(document)
    
    vectorStore= FAISS.from_documents(chunks,embedding_model)
    
    return vectorStore.as_retriever(search_kwargs= {"k":4})

acedemic_retriever= build_retriever(Path(__file__).parent/"academics_handbook.pdf")
fee_retriever= build_retriever(Path(__file__).parent/"fee_structure.pdf")

def load_context(retriever,query):
    docs= retriever.invoke(query)
    context= "\n\n".join([doc.page_content for doc in docs])
    return context 