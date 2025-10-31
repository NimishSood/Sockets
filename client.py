import socket

"""
Client: connects to the server’s IP/port and sends a message.

- If the server is on the same machine, use '127.0.0.1' (localhost).
- If the server is on your LAN, use the server’s LAN IP (e.g., 192.168.x.x).
- If the server is outside your LAN, you’d use its public IP (and the server needs port-forwarding/NAT set up).
"""
HOST = '192.168.2.10'
PORT = 65432

# One socket is enough for the client: we connect, send, receive, close.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    # Send bytes; sendall() makes sure everything goes out
    client.sendall("Hello World!".encode('utf-8'))

    # Receive up to 1024 bytes, then decode back to a string
    reply = client.recv(1024).decode('utf-8')
    print(reply)

"""
For clients, it’s just one socket.
Servers have a listening socket + a new per-connection socket returned by accept().
"""
