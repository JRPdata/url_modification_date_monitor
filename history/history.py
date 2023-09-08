import os
import json

HISTORY_DIRECTORY = os.path.join(os.path.dirname(__file__), "historydata")

def initialize_history_directory():
    # Create the history directory if it doesn't exist
    if not os.path.exists(HISTORY_DIRECTORY):
        os.makedirs(HISTORY_DIRECTORY)

def load_last_file_size(url_id):
    # Load the last file size for the given url_id
    history_file = os.path.join(HISTORY_DIRECTORY, f"{url_id}_last_file_size.json")
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history_data = json.load(file)
            return history_data.get("last_file_size")
    else:
        return None

def save_last_file_size(url_id, latest_file_size):
    # Save the latest file size for the given url_id
    history_data = {"last_file_size": latest_file_size}
    history_file = os.path.join(HISTORY_DIRECTORY, f"{url_id}_last_file_size.json")
    with open(history_file, "w") as file:
        json.dump(history_data, file)
