
""" this is the Client  for all clients connected"""


import socket
import threading

MSG_LENGHT =2048
PORT = 1234
SERVER_IP = "192.168.1.151"
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'


#ask for NICKNAME

nickname = input(" Add your Nickname of Chat :")

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
   while True:
        message = client.recv(MSG_LENGHT).decode(FORMAT)
        if message == "NICK":
            client.send(nickname.encode(FORMAT)) # send the nickname
        else:
            print(message)

def write():
    while True:
        message = input()
        message = nickname+' :'+ message
        client.send(message.encode(FORMAT))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()