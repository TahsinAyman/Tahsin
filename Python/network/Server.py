import socket
from threading import Thread

def server():
    s = socket.socket()
    host = "localhost"
    port = 9000
    while True:
        try:
            s.bind((host, port))
            s.listen(5)
            c, addr = s.accept()
            print('Got connection from', addr)
            msg = input("Enter Message: ")
            c.send(bytes(msg, 'utf8'))
        except Exception:
            pass

    s.close()

def client():
    s = socket.socket()
    host = "localhost"
    port = 8000
    try:
        s.connect((host, port))
        print(str(s.recv(1000))[2:-1])
    except Exception:
        pass
    s.close()

if __name__ == '__main__':
    thread1 = Thread(target=server)
    thread2 = Thread(target=client)

    server()
    client()

    thread1.run()
    thread2.run()


