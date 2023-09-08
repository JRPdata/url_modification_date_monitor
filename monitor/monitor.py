import os
#from config.config import load_config
import config
from config import config
from filesize import filesize
from history import history
from notify import notify

def monitor_urls():
    urls = config.initialize_urls()
    for url_data in urls:
        url_id = url_data[0]
        config_data = url_data[1]
        url = config_data['url']
        last_file_size = history.load_last_file_size(url_id)

        new_file_size = filesize.check_for_update(url_id, url, last_file_size)
        if new_file_size:
            # Create notification message
            print(url_id)
            message = notify.create_notification_message(url_id)

            # Send notification
            ntfy_url = config.load_notify()
            notify.send_notification(url_id, ntfy_url, message)

            # Update last_file_size in history
            history.save_last_file_size(url_id, new_file_size)
