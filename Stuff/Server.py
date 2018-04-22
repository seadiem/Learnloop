import os
import socket

SOCKET_FILE = './echo.socket'

if os.path.exists(SOCKET_FILE):
    os.remove(SOCKET_FILE)

print("Open UNIX socket...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(SOCKET_FILE)

print("Listen...")
i = 0
while True:
    print(i)
    i += 1
    datagram = server.recv(1024)
#    server.send("recived".encode('utf-8'))
    if not datagram:
        break
    else:
        print("-" * 20)
    print(datagram)
    if "DONE" == datagram:
        break
print("-" * 20)
print("Swich off...")
server.close()
os.remove(SOCKET_FILE)
print("Done")
