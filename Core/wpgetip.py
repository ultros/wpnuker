import socket
import sys


def get_ip(url):
    if url[:4] != "http":
        parsed_url = url.split('/')
        try:
            return socket.gethostbyname(parsed_url[0])
        except socket.gaierror:
            print(f"[!] Provide the Host portion of the url (E.g, google.com) and check if a valid domain.")
            sys.exit(1)
    else:
        return
