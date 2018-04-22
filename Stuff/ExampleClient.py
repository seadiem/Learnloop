# Echo client program
import socket


def startsocket():
    HOST = 'localhost'  # The remote host
    PORT = 50007  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall('Hello, world')
    data = s.recv(1024)
    s.close()
    print ('Received', repr(data))


class Socket:
    def __init__(self):
        SOCKET_FILE = '/Users/imac/Documents/Misc/Learn/Shared/swiftsocket'
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.s.connect(SOCKET_FILE)
    # def __init__(self):
    #     HOST = 'localhost'  # The remote host
    #     PORT = 50007  # The same port as used by the server
    #     self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self.s.connect((HOST, PORT))
    def send(self, data = ""):
        self.s.sendall(data.encode())
        size = 2 * 5000
        out = self.s.recv(size)
        return out
    def close(self):
        self.s.close()
