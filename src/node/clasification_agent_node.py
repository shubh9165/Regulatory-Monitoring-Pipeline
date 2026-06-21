from src.state.state import state
from src.llm.lamma_model import Lamma_llm
from langchain_classic.prompts import PromptTemplate


llm_obj=Lamma_llm()
model=llm_obj.get_llm()

def classification_agent(State:state):

    try:

        document = State["document"][:3000]

        prompt = f"""
        You are a Classification Agent.

        Analyze the following document and classify it into one category.

        Document:
        {document}

        Return only the category name.
        """

        response=model.invoke(prompt)

        return {"clasification_data":response.content}
    except Exception as e:
        raise ValueError(e)