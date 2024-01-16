"""
Port Scanner

Write a port scanner or detect port scanning.

1. Find open ports from 1 to 1025 range
2. Calculate time to find open ports.
"""

import socket

# Module Socket . socket class then socket method in (). AF_INET means use IPv4, then SOCK_STREAM is connection type (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "137.74.187.101" # hackthissite.org
port = 32

def portScanner(port):
    # connect_ex: like connect(address) but returns an error code instead of raising an exception when error occurs
    if s.connect_ex((host, port)):
        return f'Port {port} is closed.'
    else: # If not error code, then port is open
        return f'Port {port} is open.'

print(portScanner(port))
