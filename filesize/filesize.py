import requests
from ftplib import FTP
from urllib.parse import urlparse

def http_get_file_size(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            file_size = int(response.headers['Content-Length'])
            return file_size
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred getting {url}: {e}")
        return None

def ftp_get_file_size(url):
    parsed_url = urlparse(url)
    ftp_host = parsed_url.netloc
    ftp_path = parsed_url.path
    try:
        with FTP(ftp_host) as ftp:
            ftp.login()
            file_size = ftp.size(ftp_path)
            if file_size >= 0:
                return file_size
            else:
                return None
    except Exception as e:
        print(f"An error occurred getting {url}: {e}")
        return None

def get_file_size(url):
    if url.startswith("http://") or url.startswith("https://"):
        return http_get_file_size(url)
    elif url.startswith("ftp://"):
        return ftp_get_file_size(url)
    else:
        print("Unsupported protocol. Supported protocols are HTTP/HTTPS and FTP.")
        return None

def check_for_update(url_id, url, last_file_size):
    # Compares the last file size of a url identified by its url_id
    # with the latest file size from the history. Returns latest file size if an update is detected, None otherwise.
    latest_file_size = get_file_size(url)

    if latest_file_size and latest_file_size != last_file_size:
        return latest_file_size  # Return the new (updated) filesize
    else:
        return None
