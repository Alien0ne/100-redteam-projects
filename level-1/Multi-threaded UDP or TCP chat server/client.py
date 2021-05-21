from os import name
import socket
from sys import argv
import threading

host = "127.0.0.1"
name = argv[2]
if len(argv) != 3:
    print(f"Usage:\n\t{argv[0]} <port> <your name>")
    exit()

try:
    port = int(argv[1])
    if not (1025 < port < 65535):
        raise ValueError
except ValueError:
    print("Port must be an number between 1025 and 65535.")
    exit()


def receive():
    while True:
        try:
            data = clie.recv(4096).decode()
            check = data.lower().find("name")
            if check == -1:
                print(data)
            else:
                clie.send(name.encode())
        except:
            print("An error occured !")
            clie.close()
            break


def write():
    while True:
        message = input()
        clie.send((name+" : "+message).encode())


clie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clie.connect((host, int(argv[1])))
received_thread = threading.Thread(target=receive)
received_thread.start()
write_thread = threading.Thread(target=write)
message = write_thread.start()
