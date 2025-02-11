import socket

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345      # Port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Allow 1 connection at a time

print(f"Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)  # Receive data (max 1024 bytes)
    if not data:
        break  # Exit if no data received
    print(f"Received: {data.decode()}")