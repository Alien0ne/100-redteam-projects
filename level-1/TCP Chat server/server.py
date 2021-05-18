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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv:
    serv.bind((host, int(argv[1])))
    serv.listen()
    conn, addr = serv.accept()
    print("Connected from : ", addr)
    with conn:
        conn.send("Server Got conneted :)".encode())
        while True:
            data = conn.recv(4096).decode()
            if not data:
                break
            print("From Client :", data)
            chat.append("From Client :" + data)
            data = input("To client : ")
            conn.send(data.encode())
            chat.append("To client :" + data)
            if data.lower() == "bye":
                break
f = open("chat.txt", 'w')
with f:
    for i in chat:
        f.write(i+"\n")
