

#from socket import *		 	 # Import socket module
import sys
import ipaddress
import socket

s = socket.socket() 
host = socket.gethostname()
#host = 'localhost'    # Reading IP Address
port = 22468 

#s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port)) 			 # Bind to the port
s.listen(5) 			         # Wait for client connection.

#print("Server is running")

while True:
     conn, addr = s.accept() 		# Establish connection with client.
     print('Connected by client on', addr)

     while True:
          try:
               equation=conn.recv(1024).decode()
               if equation == "0 / 0 =":
                    conn.send("0 / 0 =".encode())
                    print('Received question', equation,';end the server program')
                    break
               else:
                    #print('Received question', equation,';send back answer', str(eval(equation)))
                    x, op, y, eql= equation.split() 
                    num1 = float (x)
                    num2 = float (y)
                    if op == '+':
                        ans = num1 + num2
                        print('Received question', equation, '; send back answer', ans)
                        #result = eval(equation)
                        #conn.send(str(result).encode())
                        conn.send(str(ans).encode())
                    elif op == '-':
                        ans = num1 - num2
                        print('Received question', equation, '; send back answer', ans)
                        conn.send(str(ans).encode())
                    elif op == '*':
                        ans = num1 * num2
                        print('Received question', equation, '; send back answer', ans)
                        conn.send(str(ans).encode())
                    elif op == '/':
                        ans = num1 / num2
                        print('Received question', equation, '; send back answer', ans)
                        conn.send(str(ans).encode())
      
          except (ArithmeticError):
               conn.send("MathError".encode())
          except (ValueError):
               conn.send("ValueError".encode())

     conn.close() 			# Close the connection.
