import socket 

HOST = socket.gethostname()
PORT = 12345

client_socket = socket.socket()
client_socket.connect((HOST, PORT))

message = "Hello, I want to aconnect"
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print(f"Message from server - {data.decode()}")