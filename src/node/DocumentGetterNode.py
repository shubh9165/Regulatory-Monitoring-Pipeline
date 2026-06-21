import requests
from bs4 import BeautifulSoup
from src.state.state import state
import os


def extract_data_node(State:state):
    try:
        website=os.getenv('website')
        url=""
        if website=='RBI':
            url="https://www.rbi.org.in/Scripts/NotificationUser.aspx"
        elif website=='SEBI':
            url="https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=1&ssid=0&smid=0"
        elif website=='IRDAI':
            url="https://irdai.gov.in/circulars"


        response=requests.get(url)
        if response.status_code==200:
            soup=BeautifulSoup(response.text,'html.parser')
        else:
            soup=f"due to error we can't load data"

        return {"document": soup.get_text(separator=" ", strip=True)}
    except Exception as e:
        raise ValueError(e)