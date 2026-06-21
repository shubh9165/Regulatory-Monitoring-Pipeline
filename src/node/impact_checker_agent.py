from src.state.state import state
from src.llm.lamma_model import Lamma_llm


llm_obj=Lamma_llm()
llm=llm_obj.get_llm()


def Impact_checker_agent(State:state):

    try:
        prompt = f"""
        You are a senior reporter.

        Based on the following new information, create a concise report
        that can be sent to a user as an update notification.

        New Data:
        {State['new_data']}

        Return only the report.
        """

        response=llm.invoke(prompt)

        return {'report':response.content}


    except Exception as e:
        raise ValueError(e)