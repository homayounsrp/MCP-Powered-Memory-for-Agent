from pydantic import BaseModel, Field
from typing_extensions import Literal

class Router(BaseModel):
    """Analyze the unread ticket and route it according to its content."""

    reasoning: str = Field(
        description="Step-by-step reasoning behind the classification."
    )
    classification: Literal["Returns & Refunds", "billing", "general"] = Field(
        description="The order of a ticket: " \
        "'Returns & Refunds' for return or refund related request, "
        "'billing' for requests about billing, "
        "'general' for general requests",
       
    )