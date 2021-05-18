import socket
from sys import argv
host = "127.0.0.1"

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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as clie:
    clie.connect((host, int(argv[1])))
    while True:
        data = clie.recv(4096).decode()
        if data.lower() == "bye":
            break
        print("From server :", data)
        data = input("To server : ")
        clie.send(data.encode())
