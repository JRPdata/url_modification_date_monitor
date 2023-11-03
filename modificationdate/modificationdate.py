import requests
from ftplib import FTP
from urllib.parse import urlparse

def http_get_modification_date(url):
    try:
        response = requests.head(url)
        # Check if the request was successful (status code 200 or 2xx)
        if response.status_code // 100 == 2:
            # Extract the modification date from the 'Last-Modified' header
            modification_date = response.headers.get('Last-Modified')
            return modification_date
        # If the request was not successful, return None
        return None

    except Exception as e:
        print(f"An error occurred getting {url}: {e}")
        return None

# must pass ftp://username:pass@host.com/path/to/file
# optionally leave out username:pass and use anonymous as default user/pass
def get_ftp_modification_date(url):
    parsed_url = urlparse(url)
    file_path = parsed_url.path
    ftp_host = parsed_url.netloc
    user_pass_host = ftp_host.split('@')
    username = 'anonymous'

    if len(user_pass_host) != 1:
        user_pass = user_pass_host[:-1]
        ftp_host = user_pass_host[-1]
        user_pass = user_pass.split(':')
        username = user_pass[0]
        if len(user_pass) == 2:
            password = user_pass[1]
        else:
            password = 'anonymous'
    else:
        password = 'anonymous'
    try:
        # Connect to the FTP server
        ftp = FTP(ftp_host)
        ftp.login(username,password)
        # Try to get the modification date using MLST
        response = ftp.sendcmd('MLST {}'.format(file_path))
        # If MLST is supported, parse the response to extract the modification date
        if response.startswith('250-'):
            lines = response.split('\n')
            for line in lines:
                parts = line.split(';')
                for part in parts:
                    field_value = part.strip().split('=', 1)
                    if len(field_value) == 2:
                        field, value = field_value
                        if field.lower() == 'modify':
                            modification_date = value
                            return modification_date
        # If MLST is not supported, fall back to using STAT
        response = ftp.sendcmd('STAT {}'.format(file_path))
        if response.startswith('2'):
            # response is not easy to parse consistently (store the entire line)
            return response
        # If neither method works, return None
        return None
    except Exception as e:
        # Handle any FTP connection or command errors here
        print("Error:", str(e))
        return None
    finally:
        try:
            ftp.quit()
        except Exception as e:
            pass

def get_modification_date(url):
    if url.startswith("http://") or url.startswith("https://"):
        return http_get_modification_date(url)
    elif url.startswith("ftp://"):
        return ftp_get_modification_date(url)
    else:
        print("Unsupported protocol. Supported protocols are HTTP/HTTPS and FTP.")
        return None

def check_for_update(url_id, url, last_modification_date):
    # Compares the last modification date of a url identified by its url_id
    # with the latest file modification date from the history. Returns latest modification if an update is detected, None otherwise.
    latest_modification_date = get_modification_date(url)

    if latest_modification_date and latest_modification_date != last_modification_date:
        return latest_modification_date  # Return the new (updated) file modification date
    else:
        return None
