import subprocess

def create_notification_message(msg):
    # Creates a notification message based on the repository ID and filtered list of files
    message = msg
    return message

def send_notification(url_id, ntfy_url, message):
    # Sends the notification message to the desired destination using the ntfy program
    command = ['ntfy', 'publish', f'{ntfy_url}/{url_id}', message]
    subprocess.run(command, check=True)
