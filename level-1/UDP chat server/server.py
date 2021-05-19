import socket
from sys import argv

host = "127.0.0.1"
chat = []

if len(argv) != 2:
    print(f"Usage:\n\t{argv[0]} <port>")
    exit()

try:
    port = int(argv[1])
    if not (1025 < port < 65535):
        raise ValueError
except ValueError:
    print("Port must be an number between 1025 and 65535.")
    exit()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as serv:
    serv.bind((host, int(argv[1])))
    while True:
        data, addr = serv.recvfrom(4096)
        print("From Client : ", data.decode())
        chat.append("From Client :" + data.decode())
        data = input("To client : ")
        chat.append("To client :" + data)
        serv.sendto(data.encode(), addr)
        if data.lower() == "bye":
            break

f = open("chat.txt", 'w')
with f:
    for i in chat:
        f.write(i+"\n")
