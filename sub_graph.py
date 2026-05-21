
from states import SubState
from nodes import write_copy, write_image_prompt, merge_results
from langgraph.graph import StateGraph, START, END

#Sub graph

#Sub graph

child = StateGraph(SubState)

child.add_node("writer", write_copy)
child.add_node("image_prompt", write_image_prompt)
child.add_node("merge", merge_results)

child.add_edge(START,"writer")
child.add_edge(START,"image_prompt")
child.add_edge("writer","merge")
child.add_edge("image_prompt","merge")
child.add_edge("merge",END)

subgraph = child.compile()