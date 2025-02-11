import socket

HOST = '127.0.0.1' #Example '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Hello world"
client_socket.sendall(message.encode())

'''
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")
'''

client_socket.close()