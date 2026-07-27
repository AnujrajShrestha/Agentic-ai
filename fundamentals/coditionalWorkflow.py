from langchain_mistralai import ChatMistralAI,MistralAIEmbeddings
from langgraph.graph import StateGraph,START,END
from typing import _TypedDict, Annotated
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import os

load_dotenv()

embedding_model= MistralAIEmbeddings(model='mistral-embed')
llm= ChatMistralAI(model='mistral-large-latest')

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

acedemic_retriever= build_retriever("academics_handbook.pdf")
fee_retriever= build_retriever("fee_structure.pdf")