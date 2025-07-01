
from langgraph.graph import StateGraph, START, END
from Graph.Nodes.Triage.triage import triage_router
from Graph.Nodes.ReACT.react import react_agent
from Graph.graph_state import State


def customer_support_agent(input, config):

    # Initialize the StateGraph
    email_agent = StateGraph(State)
    email_agent = email_agent.add_node(triage_router)
    email_agent = email_agent.add_node("response_agent", react_agent)
    email_agent = email_agent.add_edge(START, "triage_router")
    email_agent = email_agent.compile()

    # Invoke the agent with input text
    response = email_agent.ainvoke({"ticket_input": input}, config)
    return response