import os
import re

CONFIG_DIRECTORY = "conf/urls"

def load_notify():
    # Load ntfy_url from conf/ntfy_url
    with open("conf/ntfy_url", "r") as file:
        ntfy_url = file.read().strip().rstrip("/")

    return ntfy_url

def load_config(url_id):
    """
    Load the configuration data for a url.

    Args:
        url_id (str): The unique identifier for the url.

    Returns:
        dict: The configuration data for the url.
    """
    config_file = os.path.join(CONFIG_DIRECTORY, f"{url_id}.conf")
    with open(config_file, "r") as file:
        lines = file.readlines()

    url = lines[0].strip()

    return {
        "url": url
    }

def initialize_urls():
    """
    Initialize the urls to be watched.

    Returns:
        list: A list of containing the url ID and configuration data.
    """
    urls = []
    config_files = [file for file in os.listdir(CONFIG_DIRECTORY) if file.endswith(".conf")]
    for file in config_files:
        url_id = file.split(".")[0]
        config_data = load_config(url_id)
        urls.append((url_id, config_data))
    return urls
