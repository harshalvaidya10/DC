import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

client_socket.connect((host, port))

while True:
    message = input("Enter the message to be sent to the client: ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Data sent by the server:{data}")

client_socket.close()