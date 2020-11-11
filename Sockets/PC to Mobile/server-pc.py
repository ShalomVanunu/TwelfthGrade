import socket, sys, threading

LOCAL_PORT =  # Enter local port
FILENAME =  # Enter filename

s = socket.socket()
s.bind(('0.0.0.0', ))
s.listen(1)


def send_video(conn):
    with open(FILENAME, 'rb') as vid:
        data = vid.read(1024)
        while data:
            try:
                conn.send(data)
            except Exception as e:
                print(e)
                sys.exit(-1)
            try:
                data = vid.read(1024)
            except Exception as e:
                print(e)
                pass
        conn.close()


while True:
    conn, addr = s.accept()
    print(addr, "connected")

    t = threading.Thread(target=send_video, args=[conn])
    t.start()
