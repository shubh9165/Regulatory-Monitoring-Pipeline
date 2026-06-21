from src.llm.lamma_model import Lamma_llm
from src.state.state import state

llm_obj=Lamma_llm()
llm=llm_obj.get_llm()

def comparing_agents(State:state):
    try:
        prompt = f"""
        You are a data comparison agent.

        Old Data:
        {State['old_data']}

        New Data:
        {State['document']}

        Find information that exists in New Data but does not exist in Old Data.

        Return only the newly added information.
        If there are no changes, return:
        NO_CHANGES
        """

        response=llm.invoke(prompt)
        
        result = response.content.strip()

        if result == "NO_CHANGES":
            return {
                "old_data": state["document"]
            }
        

        return {
            'old_data':State['document'],
            'new_data':response.content}
    
    except Exception as e:
        raise ValueError(e)