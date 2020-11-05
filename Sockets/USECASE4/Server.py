"""
this program deals with many client issues
with thread
"""

import socket
import threading

#declare CONSTANT
MSG_LENGHT  = 1024
PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = 'exit'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr): # function deals with many client
    print(f"[NEW CONNCTION] {addr[0]} connected") # Show only IP
    connected = True

    while connected:
        msg = conn.recv(MSG_LENGHT).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f'[{addr[0]}] : {msg}')
        conn.send("MSG Received".encode(FORMAT))
    conn.close()




def start():
    server.listen()
    print(f" [LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}')


if __name__ == '__main__':
    print('[STARTING] server is on..')
    start()
