from typing import TypedDict, List
from operator import add
from langgraph.graph.message import add_messages
from typing import Annotated


class SubState(TypedDict):
    angle: str #The input, e.g., "Humorous"
    copy: str #The generated social media text
    image_prompt: str #The generated AI image prompt
    campains: list[str] #The final merged output that will eventually get passed back to the main graph

#The main state
#The main state
class MainState(TypedDict):
    product : str
    angles : List[str]
    human_feedback : str
    messages : Annotated[list, add_messages]
    campains : Annotated[list[str], add]    

print("STATES INITIALIZED")
