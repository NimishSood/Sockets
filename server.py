import socket

HOST = '192.168.2.10'  # LAN IP address of the server
PORT = 65432           # Port number to listen on

# Create an Internet (IPv4) TCP socket
# This socket is only used for accepting connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)  # Allow up to 5 pending connections before rejecting

while True:
    # Accept a new client connection
    # This returns a new socket dedicated to communicating with that client
    communication_socket, address = server.accept()
    print('Connection from', address)

    # Receive message from client (max size 1024 bytes)
    # Messages are sent as bytes, so we decode them
    message = communication_socket.recv(1024).decode()
    print(f"Message from client is:",message)

    # Send a response back to the client
    communication_socket.send("We received your message! Have a nice day :)".encode('utf-8'))
    communication_socket.close()

    print('Connection closed with', address)
