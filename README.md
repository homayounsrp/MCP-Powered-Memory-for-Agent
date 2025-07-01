# Semantic Memory - Customer Support Agent

This package implements a customer support agent workflow using LangGraph, LangChain, and memory tools. It is designed to triage, route, and respond to support tickets, leveraging LLMs and persistent memory.

## Features

- **Ticket Triage:** Automatically classifies incoming support tickets into Returns & Refunds, Billing, or General categories.
- **Automated Responses:** Uses LLMs to generate empathetic, efficient responses to customer inquiries.
- **Memory Management:** Stores and retrieves customer information and ticket history for personalized support.
- **Extensible Tools:** Integrates with custom tools for responding to tickets, scheduling callbacks, checking ticket status, and managing memory.

## Project Structure

- `config.py` - Loads environment variables and configures external services.
- `Data.py` - Example support tickets for testing.
- `graph.py` - Main workflow definition for the customer support agent.
- `prompt_templates.py` - Prompt templates for system and triage instructions.
- `util.py` - Utility functions for parsing and formatting.
- `Graph/` - Contains state definitions, memory, MCP client/server, and node logic for triage and response.
- `main.ipynb` - Example notebook demonstrating agent usage.

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

2.  **Configure environment:**

    - Copy .env and set your OPENAI_API_KEY and other required variables.

3.  **Run the agent:**

    - See main.ipynb for example usage.


## Usage Example

```python
from graph import customer_support_agent
from Data import ticket1

config = {"configurable": {"user_id": "alexsmith"}}
response = await customer_support_agent(input=ticket1, config=config)
