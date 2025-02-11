import socket

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345      # Port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
server_socket.bind((HOST, PORT))

print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        try:
            data, addr = server_socket.recvfrom(1024)  # Receive data from client
            print(f"Received from {addr}: {data.decode()}")
            server_socket.sendto(data, addr)  # Echo the message back
        except Exception as e:
            pass
            #print(e)

except KeyboardInterrupt:
    print("\nServer shutting down...")
    server_socket.close()
    
print("Exiting server.")