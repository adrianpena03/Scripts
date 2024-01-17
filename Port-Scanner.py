"""
Port Scanner

Write a port scanner or detect port scanning.

1. Find open ports from 1 to 1025 range
2. Calculate time to find open ports.
"""

import socket

# # Module Socket . socket class then socket method in (). AF_INET means use IPv4, then SOCK_STREAM is connection type (TCP)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = input("Enter a valid host IP address: ")
# port = int(input("Enter a valid port you'd like to see is open/closed: "))

# print("\nPlease wait a few moments...\n")

# def portScanner(host, port):
#     # connect_ex: like connect(address) but returns an error code instead of raising an exception when error occurs
#     if s.connect_ex((host, port)):
#         return f'Port {port} is closed.'
#     else: # If not error code, then port is open
#         return f'Port {port} is open.'

# print(portScanner(host, port))

# # ------ Second Version ------
# import datetime as dt
# curr_time = dt.datetime.now()


# ask user what host they want to scan
# as user a range of ports they want to scan (ex. between 1-5 or 23-32)
# Get current time (this will be subtracted to the time after the code finishes to get total time taken to run the script)

# start function called secondPortScanner(), takes in the 2 numbers from port ranges
# check if the user input is a valid IP address, if not then say enter valid one
# check if user input a correct port range (from 0 - 1023 (well known ports according to google)) 
# if correct, then proceed to iterate through port ranges, make suure to add +1
# if program reaches a port that is closed, return Port X is closed. Else, port X open

# I see issue though, there can only be one return statement in func. so how will it give response to all ports given one IP? Maybe store response somewhere

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter a valid host IP address: ")
port1 = int(input("Enter the first valid port you'd like to see is open/closed: "))
port2 = int(input("Enter the second valid port you'd like to see is open/closed: "))

def secondPortScanner(host, port1, port2):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    host_split = int(host.split('.'))

    # Check if user inputed valid IP
    for num in host_split:
        if num not in numbers:
            return 'Enter a valid IP address.'
        if len(host_split) < 12 or len(host_split) > 12:
            return 'Check amount of numbers in IP'
        else:
            return 'Your IP is valid. Comtinuing program ...'
    
    # Check if user inputed valid ports (between ranges 0 - 1023)
    pass

print(secondPortScanner(host, port1, port2))
