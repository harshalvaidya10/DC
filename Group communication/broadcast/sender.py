import socket 

broadcast_addr = "<broadcast>"
broadcast_port = 5000

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = "Hello World"
sender_socket.sendto(message,broadcast_addr)