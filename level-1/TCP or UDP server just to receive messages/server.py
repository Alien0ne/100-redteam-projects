import socket

host = socket.gethostname()
port = 9999

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()
conn, addr = server_socket.accept()
message = "Server Got conneted :) "
print("Conneted by : ", addr)
conn.send(message.encode())
data = conn.recv(1024)
print("From Client : ", data.decode())
message2 = input("To Client : ")
conn.send(message2.encode())
