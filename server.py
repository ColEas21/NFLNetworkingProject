
from socket import *
import sys


serverSocket = socket(AF_INET, SOCK_STREAM)

# Define the IP address and port to bind to
serverIP = '192.168.247.1'
serverPort = 6789  # You can choose any available port

# Prepare a server socket
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Accept incoming connection

    try:
        message = connectionSocket.recv(1024).decode()  # Receive data from the client
        filename = message.split()[1]
        print(f"Requested filename: {filename}")
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

serverSocket.close()
