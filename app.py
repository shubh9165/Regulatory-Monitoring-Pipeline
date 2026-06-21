from pathlib import Path
from src.graph.graph import Create_graph
from src.database.database import get_old_data,update_old_data
import os

FILE_PATH = Path("src/database/database.py")


def run_pipeline():
    agent = Create_graph()

    # Read old data
    website=os.getenv('website')
   

    data=get_old_data(website)

    initial_state = {
        "document": "",
        "clasification_data": "",
        "old_data": data,
        "new_data": "",
        "report": ""
    }

    result = agent.invoke(initial_state)

    # Save updated data
    update_old_data(website,result['old_data'])

    print("Document:")
    print(result["document"])
    print("-" * 50)

    print("Classification:")
    print(result["clasification_data"])
    print("-" * 50)

    print("New Data:")
    print(result["new_data"])
    print("-" * 50)

    print("Report:")
    print(result["report"])
    print("-" * 50)


