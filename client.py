import socket
import sys


def http_client(server_host, server_port, filename):
    # defines socket for client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client_socket.connect((server_host, server_port))
    #Requests to get file
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"

        client_socket.send(request.encode())

        # creates a system response
        response = client_socket.recv(4096)
        print(response.decode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the socket
        client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 client.py server_host server_port filename")
    else:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])
        filename = sys.argv[3]
        http_client(server_host, server_port, filename)

