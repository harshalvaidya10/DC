import socket 

HOST = socket.gethostname()
PORT = 12345

server_socket = socket.socket()
server_socket.bind((HOST, PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()

data = client_socket.recv(1024)
print(f"Message from client at Address {addr} - {data.decode()}")

message = "Received"
client_socket.sendall(message.encode())