#Aaron Moo
#Assignment 1

#from socket import *		 	 # Import socket module
import sys
import ipaddress
import operator
import socket

try:
    s = socket.socket()         # Create a socket object
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    #$host = 'localhost'    # Reading IP Address
    port = 22468          # Reading port number
    #s = socket(AF_INET, SOCK_STREAM)    
    s.connect((host, port)) # Connecting to server
    print("Connected with server on", ip)
    while(True):
        equ=input()
        #s.send(equ.encode())
        s.send(str(equ).encode())
        
        result = s.recv(1024).decode()
        if result == '0 / 0 =':
            print("User input ends; end the client program")
            sys.exit()
        elif result == "MathError":
            print("Input error. Re-type the math question again")
        elif result == "ValueError":
            print("Input error. Re-type the math question again")
        else:
            print("Answer from server:", result)

    s.close 				 # Close the socket when done

except:
    s.close()