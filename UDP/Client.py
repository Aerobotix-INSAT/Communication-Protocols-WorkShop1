import socket

HOST = '127.0.0.1'  # Server IP address (change if running on another machine)
PORT = 12345        # Must match the server’s port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket

message = "Hello world"
client_socket.sendto(message.encode(), (HOST, PORT))  # Send message to server
'''
data, _ = client_socket.recvfrom(1024)  # Receive response from server
print(f"Received from server: {data.decode()}")
'''
client_socket.close()