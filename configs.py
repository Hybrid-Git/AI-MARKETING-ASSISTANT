from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os
from langgraph.checkpoint.memory import MemorySaver
load_dotenv()

llm = ChatNVIDIA(model="meta/llama-3.1-8b-instruct",api_key=os.environ.get("NVIDIA_API_KEY"),temperature=0.60)
memory = MemorySaver()


print("LLM INITIALIZED")
print("MEMORY CHECKPOINTER INITIALIZED")