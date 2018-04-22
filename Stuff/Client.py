import os
import socket

SOCKET_FILE = './echo.socket'

print("Connect")
if os.path.exists(SOCKET_FILE):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(SOCKET_FILE)
    print("Done.")
    print("Ctrl-C for out.")
    print("'DONE' for swich off the server")
    while True:
        try:
            x = input("> ")  # for py2 use raw_input
            if "" != x:
                print("send: %s" % x)
                client.send(x.encode('utf-8'))
                datagram = client.recv(1024)
                print(datagram)
                if "DONE" == x:
                    print("Switch outing.")
                    break
        except KeyboardInterrupt as k:
            print("Switch outing.")
            break
    client.close()
else:
    print("Error Connection!")
print("Done")
