import socket

PORT = 89
FORMAT = 'ascii'
SERVER_IP = "192.168.1.1"
ADDR = (SERVER_IP, PORT) # Tupple IP, PORT

print("[Starting] Client....")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IpV4, TCP
if client.connect(ADDR) == None: # connect to IP and PORT
    print('port is open')
else:
    print('port is closed')