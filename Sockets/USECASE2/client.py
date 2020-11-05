import socket


PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.1.222"
ADDR = (SERVER, PORT)

print("[STARTING] Clinet is starting...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if client.connect(ADDR) :
    print('OK')
else:
    print('Bad')
while True:
    msg = input('[SEND MESSAGE] Type [Exit].....:')
    if msg == 'exit':
        client.send(msg.encode(FORMAT))
        client.close()
        print('[CLOSED CONNECTION]')
        break
    client.send(msg.encode(FORMAT))







