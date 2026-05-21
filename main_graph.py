from states import MainState
from nodes import reviewer, generate_angles, compile_deck, human_review, mapper, router_after_review
from langgraph.graph import StateGraph, START, END
from sub_graph import subgraph

parent = StateGraph(MainState)
parent.add_node("reviewer", reviewer)
parent.add_node("subgraph", subgraph)
parent.add_node("human_review", human_review)
parent.add_node("generate_angles", generate_angles)
parent.add_node("compile_deck", compile_deck)

parent.add_edge(START,"generate_angles")
parent.add_conditional_edges("generate_angles",mapper,["subgraph"])
parent.add_edge("subgraph","compile_deck")
parent.add_edge("compile_deck","human_review")
parent.add_conditional_edges("human_review",router_after_review,["reviewer",END])
parent.add_edge("reviewer","human_review")
maingraph = parent.compile(interrupt_before=["human_review"])