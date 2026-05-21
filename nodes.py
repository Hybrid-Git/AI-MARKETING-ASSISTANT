from states import SubState, MainState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from configs import llm
from langgraph.types import Send
from typing import Literal
#NODES FOR OUR SUB GRAPH

def write_copy(state: SubState):
    angle = state['angle']
    prompt = f"You are a content creator and your task is to write a 1-2 sentence social media post for the given angle: {angle}"
    response = llm.invoke(prompt)
    return{
        "copy": response.content
    }

def write_image_prompt(state: SubState):
    angle = state['angle']
    prompt = f"You are an AI image prompt engineer. Your task is to write a detailed Midjourney/DALL-E prompt for the given angle: {angle}"
    response = llm.invoke(prompt)
    return{
        "image_prompt": response.content
    }

def merge_results(state: SubState):
    return{
        "campains": [state["copy"], state["image_prompt"]]
    }

print("NODES INITIALIZED FOR SUB GRAPH")

def human_review(state: MainState):
    """
    This is the dummy node for our breakpoint.
    """
    pass

def generate_angles(state: MainState):
    """
    This is the node that will analyze the product and decides on 3 different marketing angles.
    """
    product = state["product"]
    prompt = f"""
    You are a marketing expert. Analyze the following product and decide on 3 different marketing angles.
    
    Product: {product}
    
    Return only a comma-separated list of the angles.(e.g., Humorous, Tech-focused, Luxury).
    """
    response = llm.invoke(prompt).content
    
    return {"angles": [a.strip() for a in response.split(",")]}

def compile_deck(state: MainState):
    """
    This is the node for our deck compilationThe Reducer Node: Gathers the parallel campaigns into one document..
    """

    deck_content = "\n".join(state["campains"])
    final_deck = f"# Marketing Deck\n\n{deck_content}"
    return {"deck": final_deck,
            "messages":[AIMessage(content=final_deck)]
            }

def reviewer(state:MainState):
    """
    The HITL Loop: Rewrites the deck based on human feedback.
    """

    sys_message = SystemMessage(content="You are a marketing expert. Revise the campaign deck based on the human feedback.")
    state["messages"].append(HumanMessage(content=state["human_feedback"]))

    response = llm.invoke([sys_message] + state["messages"])
    return {"deck": response.content,"messages":[response]}

def mapper(state:MainState):
    return [Send("subgraph",{"angle":a}) for a in state["angles"]]

def router_after_review(state:MainState) -> Literal["end","reviewer"]:
    if state["human_feedback"] == "approve":
        return END
    else:
        return "reviewer"

print("NODES INITIALIZED FOR MAIN GRAPH")
