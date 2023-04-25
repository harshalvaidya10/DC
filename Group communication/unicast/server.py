import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port  = 12345

server_socket.bind((host, port))

server_socket.listen(1)

client_socket, addr = server_socket.accept()
print(f"connected to {addr}")

while True: 
    data = client_socket.recv(1024)
    if not data:
        break 
    print(f"Data recieved from client:{data.decode}")
    client_socket.send(data)

client_socket.close()