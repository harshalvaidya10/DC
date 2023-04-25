import socket 

receiver_port = 5000
receiver_addr = ""

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

receiver_socket.bind(receiver_addr, receiver_port)

data, addr = receiver_socket.recvfrom(1024)
print(f"Data received from {addr} is {data.decode()}")