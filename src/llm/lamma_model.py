from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv('GROQ_API_KEY')

class Lamma_llm():

    def get_llm(self):
        try:
            llm=ChatGroq(model='llama-3.3-70b-versatile',api_key=api_key)

            return llm

        except Exception as e:
            raise ValueError(e)
