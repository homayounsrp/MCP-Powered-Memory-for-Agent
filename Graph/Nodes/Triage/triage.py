
from langchain.chat_models import init_chat_model
from Graph.Nodes.Triage.output_parser import Router
from config import get_openai_api_key
from Graph.graph_state import State
from langgraph.types import Command
from typing import Literal
from prompt_templates import triage_system_prompt, triage_user_prompt
from Graph.Nodes.Triage.prompts import prompt_instructions
from langgraph.graph import END

llm = init_chat_model("openai:gpt-4o-mini")
llm_router = llm.with_structured_output(Router)
# ================
def triage_router(state: State) -> Command[
    Literal["response_agent", "__end__"]
]:
    
    customer_name = state['ticket_input']['from']
    subject = state['ticket_input']['subject']
    ticket_description = state['ticket_input']['ticket_description']





    system_prompt = triage_system_prompt.format(
    triage_returns_refunds=prompt_instructions["triage_rules"]["Returns & Refunds"],
    triage_billing=prompt_instructions["triage_rules"]["billing"],
    triage_general=prompt_instructions["triage_rules"]["general"],
    examples=None,
    
    )
    user_prompt = triage_user_prompt.format(
        customer_name=customer_name, 
        subject=subject, 
        ticket_description=ticket_description
    )





    # calling triage model to classify the email
    result = llm_router.invoke(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )
    # if triage classification is "Returns & Refunds", "billing", or "general", route to the appropriate agent
    if result.classification == "Returns & Refunds":
        print("🔄 Classification: RETURNS & REFUNDS - Route to returns/refunds agent")
        goto = "response_agent"
        update = {
            "messages": [
                {
                    "role": "user",
                    "content": f"Handle returns/refunds for ticket: {state['ticket_input']}",
                }
            ]
        }
    elif result.classification == "billing":
        print("💳 Classification: BILLING - Route to billing agent")
        goto = "billing_agent"
        update = {
            "messages": [
                {
                    "role": "user",
                    "content": f"Handle billing for ticket: {state['ticket_input']}",
                }
            ]
        }
    elif result.classification == "general":
        print("📋 Classification: GENERAL - Route to general agent")
        goto = "general_agent"
        update = {
            "messages": [
                {
                    "role": "user",
                    "content": f"Handle general inquiry for ticket: {state['ticket_input']}",
                }
            ]
        }
    else:
        raise ValueError(f"Invalid classification: {result.classification}")
    return Command(goto=goto, update=update)