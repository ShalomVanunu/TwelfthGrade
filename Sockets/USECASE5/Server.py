

""" this is the Server broadcat data to all clients connected"""

import socket
import threading

MSG_LENGHT =2048
PORT = 1234
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# list of all clients
clients = []
nicknames = []

#strat Server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

# this function send message to all clients
def broadcast(message):
    for client in clients:
        client.send(message.encode(FORMAT))


# Handle the message from clients
def handle(client):
    while True:
        message = client.recv(MSG_LENGHT).decode(FORMAT)
        broadcast(message)


# deal with data from clients
def receive():
    while True:
        client, address = server.accept()
        print(f"[Connected] connected with {address}")

        client.send('NICK'.encode(FORMAT))
        nickname = client.recv(MSG_LENGHT).decode(FORMAT)
        nicknames.append(nickname) # list of Nickname of clients
        clients.append(client) # list of Obj clients

        # broadcast the connection of clients
        print(f" NickName {nickname} is connected")
        broadcast(f" {nickname} Joined! \n")

        # Handle the client for send and receive data
        thread  = threading.Thread(target=handle , args=(client,))
        thread.start()





if __name__ == "__main__":
    receive()