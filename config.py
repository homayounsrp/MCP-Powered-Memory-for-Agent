import os
from dotenv import load_dotenv, find_dotenv
            

from langchain_neo4j import Neo4jGraph
from neo4j.debug import watch

                                                                                                                    # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key



def load_neo4j_graph() -> Neo4jGraph:
    load_env()
    uri      = os.getenv("NEO4J_URI")
    user     = os.getenv("NEO4J_USERNAME")
    password = os.getenv("NEO4J_PASSWORD")
    database = os.getenv("NEO4J_DATABASE", "neo4j")

    graph = Neo4jGraph(
        url=uri,
        username=user,
        password=password,
        database=database,
    )
    return graph
