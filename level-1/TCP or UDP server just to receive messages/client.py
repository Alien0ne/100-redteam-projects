import socket

host = socket.gethostname()
port = 9999

client_socket = socket.socket()
client_socket.connect((host, port))

data = client_socket.recv(1024)
print("From server : ", data.decode())
message = input("To server : ")
client_socket.send(message.encode())
data = client_socket.recv(1024)
print("From server : ", data.decode())
