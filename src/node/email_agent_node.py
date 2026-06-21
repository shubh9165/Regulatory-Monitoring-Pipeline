from src.state.state import state
from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def email_agent(State:state):

    try:

        if "NO_CHANGES" in State["new_data"]:
            return State
        
        sender=os.getenv('sender')
        password=os.getenv('password')

        receiver=os.getenv('receiver')
        
        msg=MIMEText(State['report'])

        msg["subject"]=f"Regularity update-{State['clasification_data']}"
        msg["sender"]=sender
        msg["receiver"]=receiver

        server=smtplib.SMTP("smtp.gmail.com",587)

        server.starttls()

        server.login(sender,password)

        server.sendmail(
            sender,
            receiver,
            msg.as_string()
        )

        server.quit()

        return State

        

    except Exception as e:
        raise ValueError(e)