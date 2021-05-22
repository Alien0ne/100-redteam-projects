import socket
from sys import argv
import threading


host = "127.0.0.1"
running = True
clients = []
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


def client_thread(conn, addr, name, clients):
    global running
    while running:
        try:
            data = conn.recv(4096).decode()

            chat.append(data)
            for client in clients:
                client.send(data.encode())
            if "bye" in data:
                clients.remove(conn)
                conn.close()
                running = False
        except:
            print(clients)
            print(conn)
            index = clients.index(conn)
            clients.remove(conn)
            conn.close()


serv = socket.socket()
serv.settimeout(5)
serv.bind((host, int(argv[1])))
serv.listen(5)
print("Listening for connections ...")
while running:
    try:
        conn, addr = serv.accept()
    except socket.timeout:
        continue
    clients.append(conn)
    print("No of clients : ", len(clients))
    conn.send("Connected To Server :)\n".encode())
    conn.send("Enter your Name : ".encode())
    name = conn.recv(2046).decode()
    print("Conneted By : " + name + ", Address : " + str(addr))
    thread = threading.Thread(
        target=client_thread, args=(conn, addr, name, clients))
    thread.start()
    if len(clients) == 0:
        running = False


f = open("chat.txt", 'w')
with f:
    for i in chat:
        f.write(i+"\n")
