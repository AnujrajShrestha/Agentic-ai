import os
from typing import TypedDict

#Lets create the state first
class pipelineState(TypedDict):
    raw_input: str
    edited_text: str
    script_text: str
    final_output: str

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

llm= ChatMistralAI(model= "mistral-large-latest",temperature=0.7)

def editor_node(state: pipelineState) -> dict:
    """Stage 1: Cleans up grammar, removes typos, and refines the tone."""
    
    prompt=(
        "You are an expert copyeditor. Clean up the following raw text."
        "Fix any grammatical errors, spelling mistakes, and smooth out the transition flow"
        "while keeping the core messages intact. Return only the edited text.\n\n"
        f"Text:\n{state['raw_input']}"
    )
    response= llm.invoke(prompt)
    return {
        'edited_text': response.content.strip()
    }
    
def scriptwriter_node(state: pipelineState) -> dict:
    """Stage 2: Formats the clean text into an engaging video script video script style."""
    print("\n--- [stage 2] Executing Scriptwritting Node ---")
    
    prompt= (
        "You are a charismatic Youtube content creator. Take this edited text and transform"
        "it into a highly engaging, punchy, conersational video script hook. make it sound"
        "like a real preson speaking passionately. Return only the script content.\n\n"
        f"Edited Text:\n{state['edited_text']}"
    )
    
    response= llm.invoke(prompt)
    return {
        'script_text': response.content.strip()
    }
    
def translator_node(state: pipelineState) -> dict:
    """Stage 3 : Translates the script into natural Nepanglish (Romanized Nepali)"""
    print("Stage 3 : Executing Translator Node")
    
    prompt = (
        "You are an expert translator specializing in informal spoken communication. "
        "Translate the following script into natural, conversational Nepanglish "
        "(Nepali written in the Roman/English alphabet). Keep the tone friendly, "
        "engaging, and easy to speak out loud.\n\n"
        f"Text:{state['script_text']}"
    )
    
    response = llm.invoke(prompt)
    
    return {"final_output": response.content.strip()}

#now your state and nodes are ready and now it is time to create the graph
#and for that graph you have to connect tese nodes and for that you have
#to use the edges
#edges are very important to create the workflows

from langgraph.graph import StateGraph, START,END

#create the graph
graph= StateGraph(pipelineState)

#add the nodes in our graph
graph.add_node("editor",editor_node)
graph.add_node("scriptwriter",scriptwriter_node)
graph.add_node("translator",translator_node)

#add edges (sequwntial- one after another)
graph.add_edge(START,"editor")
graph.add_edge("editor","scriptwriter")
graph.add_edge("scriptwriter","translator")
graph.add_edge("translator",END)

#compile the graph
app= graph.compile()
result= app.invoke({
    'raw_input': "AI Agents are the future of tech. They can think plan & act on their own. Langgraph helps you build these agents with peoper control & memory" 
})

#output
print("your result are: \n\n")
print(result['final_output'])