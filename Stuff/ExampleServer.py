# Echo server program
import socket
import os

def socketrun(handler):
    SOCKET_FILE = '/Users/imac/Documents/Misc/Learn/Shared/pythonserver'

    if os.path.exists(SOCKET_FILE):
        os.remove(SOCKET_FILE)

    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = 50007  # Arbitrary non-privileged port

    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(SOCKET_FILE)
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        try:
            data = conn.recv(1024 * 10)
        except:
            conn.close()
            s.close()
            os.remove(SOCKET_FILE)
        else:
            print("count: %s, from client: %s" % (0, data))
            if data == "DONE": break
            if not data: break
            conn.sendall("He he".encode('utf-8'))
            set = handler(data)
            return set
    print("now end")
    conn.close()
    s.close()
    os.remove(SOCKET_FILE)

