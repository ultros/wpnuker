import socket


def get_ip(url):
    if url[:4] != "http":
        return socket.gethostbyname(url)
    else:
        return "Remove protocol (http/https) from URL and retry."
