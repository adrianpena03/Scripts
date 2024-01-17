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
port1 = int(input('Enter valid port number in range of 0 and 1023 for port #1: '))


"""


WORK IN PROGRESS


"""

def secondPortScanner(host, port1):
    numbers = [str(i) for i in range(10)]
    # Validate IP address
    ip_parts = host.split('.')
    if len(ip_parts) != 3 or any(part not in numbers or not 0 <= int(part) <= 255 for part in ip_parts):
        return 'Enter a valid IP address.'

    print('Your IP is valid. Continuing program...')
    
    # Check if user inputed valid ports (between ranges 0 - 1023)
    if not 0 <= port1 <= 1023:
        return 'Enter a port number in the ranges of 0 and 1023.'
    else:
        print("\n---Continuing program---\n")
        ask_port2 = input("Do you want to include a range of ports to scan? Y/n")
        if 'y' or 'yes' in ask_port2.lower():
            port2 = int(input('Enter valid port number in range of 0 and 1023 for port #2.'))
            if port2 <= port1 or port2 > 1023:
                return 'Port number 2 should be greater than the value of port 1 and less than 1023.'
            port2 = ask_port2

            # start scanning for range of port1 to port2
            print("\nScanning ports...\n")
            for i in range(port1, port2 + 1):
                if socket.connect_ex((host, i)):
                    print(f'Port {i} is closed.')
                else: 
                    print(f'Port {i} is open.')

        if 'n' or 'no' in ask_port2.lower():
            print("Scanning with only one port.")
            if socket.connect_ex((host, port1)):
                return f'Port {port1} is closed.'
            else: # If not error code, then port is open
                return f'Port {port1} is open.'
    
print(secondPortScanner(host, port1))
# Next steps: Fix logic for ports. Also, either make port int definition outside or inside function.