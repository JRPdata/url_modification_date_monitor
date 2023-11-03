import os
import json

HISTORY_DIRECTORY = os.path.join(os.path.dirname(__file__), "historydata")

def initialize_history_directory():
    # Create the history directory if it doesn't exist
    if not os.path.exists(HISTORY_DIRECTORY):
        os.makedirs(HISTORY_DIRECTORY)

def load_last_modification_date(url_id):
    # Load the last modification date for the given url_id
    history_file = os.path.join(HISTORY_DIRECTORY, f"{url_id}_last_modification_date.json")
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history_data = json.load(file)
            return history_data.get("last_modification_date")
    else:
        return None

def save_last_modification_date(url_id, latest_modification_date):
    # Save the latest modification date for the given url_id
    history_data = {"last_modification_date": latest_modification_date}
    history_file = os.path.join(HISTORY_DIRECTORY, f"{url_id}_last_modification_date.json")
    with open(history_file, "w") as file:
        json.dump(history_data, file)
