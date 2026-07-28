from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from typing import TypedDict,Annotated
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages

from db import load_context,acedemic_retriever,fee_retriever

load_dotenv()

llm= ChatMistralAI(model='mistral-large-latest',temperature=0.4)
#step 1- State
class State(TypedDict):
    programme: str
    messages: Annotated[list,add_messages]
    query_type: str
    retrievered_context: str

#step 2- Nodes generation
def classifier_node(state: State) -> dict:
    """Look at the latest user message and decide which path to take."""
    
    last_message= state['messages'][-1].content
    
    prompt = (
        "Classify the following student query into exactly one category: "
        "'academic', 'fee', or 'general'.\n\n"
        "Use 'academic' for questions about attendance, exams, grading, credits, "
        "promotion, course structure, summer training, or degree requirements.\n"
        "Use 'fee' for questions about tuition, payment, refund, late charges, "
        "scholarships, or any money-related topic.\n"
        "Use 'general' for greetings, casual talk, or anything not related to "
        "the college rules or fee.\n\n"
        f"Query: {last_message}\n\n"
        "Return only one word: academic, fee, or general."
    )
    response= llm.invoke(prompt)
    category= response.content.strip().lower()
    
    if "academic" in category:
        category= "academic"
    elif "fee" in category:
        category= "fee"
    else:
        category= "general"
        
    return {'query_type': category}

def academic_rag_node(state: State) -> dict:
    """Retrieves relevant chunks from the academics handbook."""
    query= state['messages'][-1].content
    context= load_context(acedemic_retriever,query)
    return {'retrievered_context': context}

def fee_rag_node(state: State) -> dict:
    """Retrieves relevant chunks from the fee structure PDF."""
    query = state["messages"][-1].content
    context = load_context(fee_retriever,query)
    return {"retrievered_context": context}

def general_node(state: State) -> dict:
    """Answers directly using the LLM's own knowledge, no retrieval needed."""
    return {"retrievered_context": "No retrieval needed"}

def response_node(state: State) -> dict:
    """Generates the final answer, personalized using the student's programme."""
    query = state["messages"][-1].content
    programme = state.get("programme", "Unknown")
    context = state["retrievered_context"]

    if context == "NO_RETRIEVAL_NEEDED":
        prompt = (
            f"You are a friendly college assistant talking to a {programme} student. "
            f"Answer this question using your own general knowledge:\n\n{query}"
        )
    else:
        prompt = (
            f"You are a college assistant helping a {programme} student. "
            f"Use the following context from the official college documents to answer "
            f"the question accurately. If the context mentions specific figures for "
            f"different programmes, highlight the one relevant to {programme} if possible.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\n\n"
            f"Give a clear, friendly, and precise answer."
        )

    response = llm.invoke(prompt)
    return {"messages": [("assistant", response.content.strip())]}


def router_query(state: State):
    if state['query_type']== 'academic':
        return 'academic_rag'
    elif state['query_type']== "fee":
        return "fee_rag"
    else:
        return 'general'
    
#step 5- Building the graph
graph= StateGraph(State)
graph.add_node("classifier",classifier_node)
graph.add_node("academic_rag",academic_rag_node)
graph.add_node("fee_rag",fee_rag_node)
graph.add_node("general",general_node)
graph.add_node("response",response_node)    

#edges
graph.add_edge(START,"classifier")
graph.add_conditional_edges("classifier",router_query)
graph.add_edge("academic_rag","response")
graph.add_edge("fee_rag","response")
graph.add_edge("general","response")

graph.add_edge("response",END)

app= graph.compile()
