# AI Marketing Campaign Generator using LangGraph

An AI-powered marketing campaign generator built with **LangGraph**, **LangChain**, and **NVIDIA AI Endpoints**.

This project demonstrates how to build a structured AI workflow using a parent graph, subgraph, parallel execution, state management, and human-in-the-loop review. The system takes a product as input, generates multiple marketing angles, creates campaign content for each angle, and compiles everything into a final marketing deck.

---

## Project Description

The AI Marketing Campaign Generator is designed to show how LangGraph can be used to build more advanced AI workflows beyond a simple chatbot.

Instead of asking one LLM to perform the entire task, the workflow is divided into smaller specialized nodes. Each node handles a specific responsibility such as generating marketing angles, writing social media copy, creating image prompts, merging results, compiling the final deck, and revising the output based on human feedback.

This makes the project easier to understand, debug, and extend.

---

## Features

- Generates multiple marketing angles for a product
- Uses a parent graph to control the full workflow
- Uses a subgraph to generate campaign content for each angle
- Runs social media copy generation and image prompt generation in parallel
- Uses reducers to merge results from parallel graph executions
- Includes a human-in-the-loop review step
- Supports feedback-based revision of the final campaign deck
- Uses NVIDIA AI Endpoints as the LLM provider
- Built with a modular Python project structure

---

## Tech Stack

- Python
- LangGraph
- LangChain
- LangChain NVIDIA AI Endpoints
- NVIDIA LLM API
- Python Dotenv
- LangGraph CLI

---

## Project Structure

```text
.
├── configs.py          # LLM and memory/checkpointer configuration
├── states.py           # Main graph and subgraph state schemas
├── nodes.py            # Node functions used by the graph
├── sub_graph.py        # Subgraph for campaign generation
├── main_graph.py       # Parent graph orchestration
├── langgraph.json      # LangGraph CLI configuration
├── requirements.txt    # Project dependencies
└── proj.ipynb          # Testing notebook
```

---

## How It Works

The workflow follows this process:

```text
Product Input
     |
     v
Generate Marketing Angles
     |
     v
Send Each Angle to Subgraph
     |
     v
Generate Copy + Image Prompt in Parallel
     |
     v
Merge Campaign Outputs
     |
     v
Compile Final Marketing Deck
     |
     v
Human Review
     |
     |---- Approve ----> End
     |
     |---- Feedback ---> Revise Deck
```

---

## Main Graph Workflow

The main graph is responsible for the overall orchestration.

It performs the following steps:

1. Takes a product as input.
2. Generates different marketing angles.
3. Sends each angle to the subgraph.
4. Collects campaign outputs from all subgraph runs.
5. Compiles the final marketing deck.
6. Pauses for human review.
7. Revises the deck if feedback is provided.
8. Ends when the user approves the output.

---

## Subgraph Workflow

The subgraph handles campaign generation for a single marketing angle.

For each angle, it performs two tasks in parallel:

1. Generate social media copy.
2. Generate an AI image prompt.

After both outputs are created, the subgraph merges them into a campaign result.

```text
START
  |
  |----------------------|
  v                      v
Write Copy        Write Image Prompt
  |                      |
  |----------------------|
             v
        Merge Results
             |
             v
            END
```

---

## Example Use Case

Input product:

```text
Eco-friendly smart water bottle
```

Generated marketing angles:

```text
Eco-friendly, Tech-focused, Lifestyle
```

Possible output:

```markdown
# Marketing Deck

Eco-friendly Campaign:
Stay hydrated while helping the planet with a reusable smart bottle designed for a greener lifestyle.

Image Prompt:
A premium reusable smart water bottle placed in a natural outdoor setting with green leaves, clean sunlight, and water droplets.

Tech-focused Campaign:
Track your hydration goals with a smart bottle that reminds you when it is time to drink water.

Image Prompt:
A futuristic smart water bottle glowing with hydration tracking icons beside a smartphone app interface.

Lifestyle Campaign:
Make hydration part of your daily routine with a bottle that looks stylish, feels smart, and keeps you on track.

Image Prompt:
A stylish person carrying a smart water bottle during a morning walk in an urban park with bright natural lighting.
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

For Linux or macOS:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory and add your NVIDIA API key:

```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

---

## Running the Project

If using LangGraph CLI:

```bash
langgraph dev
```

You can also import and run the graph in Python:

```python
from main_graph import maingraph

config = {
    "configurable": {
        "thread_id": "marketing-campaign-demo"
    }
}

result = maingraph.invoke(
    {
        "product": "Eco-friendly smart water bottle",
        "human_feedback": "",
        "messages": [],
        "campaigns": []
    },
    config=config
)

print(result)
```

---

## Key LangGraph Concepts Demonstrated

This project demonstrates:

- StateGraph
- Parent graph
- Subgraph
- Parallel node execution
- Conditional edges
- Fan-out pattern using `Send`
- Reducers using `Annotated`
- Human-in-the-loop interrupts
- LLM-powered nodes
- State-based workflow design

---

## What I Learned

While building this project, I practiced:

- Designing AI workflows using LangGraph
- Breaking large tasks into smaller graph nodes
- Creating reusable subgraphs
- Managing state between nodes
- Running parallel branches
- Combining outputs using reducers
- Adding a human review step
- Using LLMs inside graph nodes
- Structuring a Python AI project for GitHub

---

## Future Improvements

Possible future improvements include:

- Add a Streamlit web interface
- Export the final marketing deck as a PDF
- Use Pydantic for structured LLM output
- Add better validation for generated angles
- Save campaign history in a database
- Add support for multiple LLM providers
- Integrate image generation APIs
- Add authentication and user sessions
- Add campaign versioning and editing

---

## Author

**Yash Sheth**

GitHub: [Hybrid-Git](https://github.com/Hybrid-Git)

---

## Disclaimer

This project is created for learning and portfolio purposes. It demonstrates how LangGraph can be used to build structured AI workflows with subgraphs, parallel execution, and human-in-the-loop review.

---

## Support

If you found this project helpful, consider giving it a star on GitHub.
