import socket
from sys import argv
import threading

host = "127.0.0.1"

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

name = argv[2]
running = True


def receive():
    global running
    while running:
        try:
            data = clie.recv(4096).decode()
            if "name" in data.lower():
                clie.send(name.encode())
            else:
                print(data)

        except:
            print("An error occured !")
            clie.close()
            break


def write():
    global running
    while running:
        message = input()
        clie.send((name+" : "+message).encode())
        if "bye" in message:
            running = False


clie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clie.connect((host, int(argv[1])))
received_thread = threading.Thread(target=receive)
received_thread.start()
write_thread = threading.Thread(target=write)
message = write_thread.start()
