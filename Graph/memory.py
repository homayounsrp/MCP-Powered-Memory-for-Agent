from langgraph.store.memory import InMemoryStore


store = InMemoryStore(
    index={"embed": "openai:text-embedding-3-small"}
)

