from src.state.state import state
from langgraph.graph import StateGraph,START,END
from src.node.DocumentGetterNode import extract_data_node
from src.node.clasification_agent_node import classification_agent
from src.node.comparing_agent import comparing_agents
from src.node.impact_checker_agent import Impact_checker_agent
from src.node.email_agent_node import email_agent

def Create_graph():

    try:
        graph=StateGraph(state)

        graph.add_node('Data_extractor',extract_data_node)
        graph.add_node('classification_agent',classification_agent)
        graph.add_node('comparing_agent',comparing_agents)
        graph.add_node('impact_checker_agent',Impact_checker_agent)
        graph.add_node('email_agent',email_agent)


        graph.add_edge(START,'Data_extractor')
        graph.add_edge('Data_extractor','classification_agent')
        graph.add_edge('classification_agent','comparing_agent')
        graph.add_edge('comparing_agent','impact_checker_agent')
        graph.add_edge('impact_checker_agent','email_agent')
        graph.add_edge('email_agent',END)


        agent=graph.compile()

        return agent
    



    except Exception as e:
        raise ValueError(e)