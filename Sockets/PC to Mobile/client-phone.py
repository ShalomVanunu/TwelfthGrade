import socket, sys

SERVER_IP =  # Enter host address
SERVER_PORT =  # Enter host port
FILENAME =  # Enter filename

s = socket.socket()
connected = False
while not connected:
    try:
        s.connect(('83.130.129.147', 21151))
        connected = True
    except Exception as e: print(e)


with open(FILENAME, 'wb') as vid:
    try:
        data = s.recv(1024)
    except Exception as e:
        print(e)
        sys.exit(-1)
    while data:
        vid.write(data)
        try:
            data = s.recv(1024)
        except Exception as e:
            print(e)
            sys.exit(-1)
